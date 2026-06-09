Debugger Sessions:
==================

Please select a debuge session type:

{% for label,entry_point in options.iteritems() %}
    {{ loop.index }}. {{label}} 
{% endfor %}


