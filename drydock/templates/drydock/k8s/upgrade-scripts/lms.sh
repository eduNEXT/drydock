{%- if 'maple' in get_upgrade_list() %}
./manage.py lms backpopulate_user_tours
{%- endif %}
{%- if 'nutmeg' in get_upgrade_list() %}
./manage.py lms compute_grades -v1 --all_courses
{%- endif %}
