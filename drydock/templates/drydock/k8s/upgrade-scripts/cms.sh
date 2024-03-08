{%- if 'maple' in get_upgrade_list() %}
./manage.py cms backfill_course_tabs
./manage.py cms simulate_publish
{%- endif %}
