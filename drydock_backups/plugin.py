from __future__ import annotations

import os
import os.path
from glob import glob

import click
import pkg_resources
from tutor import hooks

from .__about__ import __version__

config = {
    "defaults": {
        "VERSION": __version__,
        "IMAGE": "ednxops/shipyard-utils:v1.0.0",
        "CRON_SCHEDULE": '0 2 * * *',
        "AWS_ACCESS_KEY": "",
        "AWS_SECRET_KEY": "",
        "BUCKET_NAME": "",
        "BUCKET_PATH": "backups",
        "CUSTOM_STORAGE_ENDPOINT": None,
        "K8S_USE_EPHEMERAL_VOLUMES": False,
        "K8S_EPHEMERAL_VOLUME_SIZE": "8Gi",
        "MYSQL_USERNAME": '{{ MYSQL_ROOT_USERNAME }}',
        "MYSQL_PASSWORD": '{{ MYSQL_ROOT_PASSWORD }}',
        "MONGO_PASSWORD": '{{ MONGODB_PASSWORD }}',
        "MONGO_USERNAME": '{{ MONGODB_USERNAME }}'
    },
}

hooks.Filters.CONFIG_DEFAULTS.add_items(
    [
        (f"BACKUP_{key}", value)
        for key, value in config.get("defaults", {}).items()
    ]
)

hooks.Filters.CONFIG_UNIQUE.add_items(
    [
        (f"BACKUP_{key}", value)
        for key, value in config.get("unique", {}).items()
    ]
)

hooks.Filters.CONFIG_OVERRIDES.add_items(
    list(config.get("overrides", {}).items())
)


########################################
# INITIALIZATION TASKS
########################################

# To add a custom initialization task, create a bash script template under:
# drydock_backups/templates/drydock-backups/jobs/init/
# and then add it to the MY_INIT_TASKS list. Each task is in the format:
# ("<service>", ("<path>", "<to>", "<script>", "<template>"))
MY_INIT_TASKS: list[tuple[str, tuple[str, ...]]] = [
    # For example, to add LMS initialization steps, you could add the script template at:
    # drydock_backups/templates/drydock-backups/jobs/init/lms.sh
    # And then add the line:
    ### ("lms", ("drydock-backups", "jobs", "init", "lms.sh")),
]


# For each task added to MY_INIT_TASKS, we load the task template
# and add it to the CLI_DO_INIT_TASKS filter, which tells Tutor to
# run it as part of the `init` job.
for service, template_path in MY_INIT_TASKS:
    full_path: str = pkg_resources.resource_filename(
        "drydock_backups", os.path.join("templates", *template_path)
    )
    with open(full_path, encoding="utf-8") as init_task_file:
        init_task: str = init_task_file.read()
    hooks.Filters.CLI_DO_INIT_TASKS.add_item((service, init_task))


########################################
# DOCKER IMAGE MANAGEMENT
########################################


# Images to be built by `tutor images build`.
# Each item is a quadruple in the form:
#     ("<tutor_image_name>", ("path", "to", "build", "dir"), "<docker_image_tag>", "<build_args>")
hooks.Filters.IMAGES_BUILD.add_items(
    [
        # To build `myimage` with `tutor images build myimage`,
        # you would add a Dockerfile to templates/drydock-backups/build/myimage,
        # and then write:
        ### (
        ###     "myimage",
        ###     ("plugins", "drydock-backups", "build", "myimage"),
        ###     "docker.io/myimage:{{ DRYDOCK_BACKUPS_VERSION }}",
        ###     (),
        ### ),
    ]
)


# Images to be pulled as part of `tutor images pull`.
# Each item is a pair in the form:
#     ("<tutor_image_name>", "<docker_image_tag>")
hooks.Filters.IMAGES_PULL.add_items(
    [
        # To pull `myimage` with `tutor images pull myimage`, you would write:
        ### (
        ###     "myimage",
        ###     "docker.io/myimage:{{ DRYDOCK_BACKUPS_VERSION }}",
        ### ),
    ]
)


# Images to be pushed as part of `tutor images push`.
# Each item is a pair in the form:
#     ("<tutor_image_name>", "<docker_image_tag>")
hooks.Filters.IMAGES_PUSH.add_items(
    [
        # To push `myimage` with `tutor images push myimage`, you would write:
        ### (
        ###     "myimage",
        ###     "docker.io/myimage:{{ DRYDOCK_BACKUPS_VERSION }}",
        ### ),
    ]
)


########################################
# TEMPLATE RENDERING
# (It is safe & recommended to leave
#  this section as-is :)
########################################

hooks.Filters.ENV_TEMPLATE_ROOTS.add_items(
    # Root paths for template files, relative to the project root.
    [
        pkg_resources.resource_filename("drydock_backups", "templates"),
    ]
)

hooks.Filters.ENV_TEMPLATE_TARGETS.add_items(
    # For each pair (source_path, destination_path):
    # templates at ``source_path`` (relative to your ENV_TEMPLATE_ROOTS) will be
    # rendered to ``source_path/destination_path`` (relative to your Tutor environment).
    # For example, ``drydock_backups/templates/drydock-backups/build``
    # will be rendered to ``$(tutor config printroot)/env/plugins/drydock-backups/build``.
    [
        ("drydock-backups/build", "plugins"),
        ("drydock-backups/apps", "plugins"),
    ],
)


########################################
# PATCH LOADING
# (It is safe & recommended to leave
#  this section as-is :)
########################################

# For each file in drydock_backups/patches,
# apply a patch based on the file's name and contents.
for path in glob(
    os.path.join(
        pkg_resources.resource_filename("drydock_backups", "patches"),
        "*",
    )
):
    with open(path, encoding="utf-8") as patch_file:
        hooks.Filters.ENV_PATCHES.add_item((os.path.basename(path), patch_file.read()))


########################################
# CUSTOM JOBS (a.k.a. "do-commands")
########################################

# A job is a set of tasks, each of which run inside a certain container.
# Jobs are invoked using the `do` command, for example: `tutor local do importdemocourse`.
# A few jobs are built in to Tutor, such as `init` and `createuser`.
# You can also add your own custom jobs:

# To add a custom job, define a Click command that returns a list of tasks,
# where each task is a pair in the form ("<service>", "<shell_command>").
# For example:
### @click.command()
### @click.option("-n", "--name", default="plugin developer")
### def say_hi(name: str) -> list[tuple[str, str]]:
###     """
###     An example job that just prints 'hello' from within both LMS and CMS.
###     """
###     return [
###         ("lms", f"echo 'Hello from LMS, {name}!'"),
###         ("cms", f"echo 'Hello from CMS, {name}!'"),
###     ]


# Then, add the command function to CLI_DO_COMMANDS:
## hooks.Filters.CLI_DO_COMMANDS.add_item(say_hi)

# Now, you can run your job like this:
#   $ tutor local do say-hi --name="Atlas"


#######################################
# CUSTOM CLI COMMANDS
#######################################

# Your plugin can also add custom commands directly to the Tutor CLI.
# These commands are run directly on the user's host computer
# (unlike jobs, which are run in containers).

# To define a command group for your plugin, you would define a Click
# group and then add it to CLI_COMMANDS:


### @click.group()
### def drydock-backups() -> None:
###     pass


### hooks.Filters.CLI_COMMANDS.add_item(drydock-backups)


# Then, you would add subcommands directly to the Click group, for example:


### @drydock-backups.command()
### def example_command() -> None:
###     """
###     This is helptext for an example command.
###     """
###     print("You've run an example command.")


# This would allow you to run:
#   $ tutor drydock-backups example-command
