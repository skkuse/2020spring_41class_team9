from django import forms

class CounterTextInput(forms.TextInput):
    template_name = "widgets/counter_text.html"

"""
<!-- templates/widgets/counter_text.html -->

{% include "django/forms/widgets/input.html" %}

<span id="counter_{{widget.attrs.id}}"></span>

<script>
    document.querySelector('#{{widget.attrs.id}}').addEventListener("input", function(){
        document.querySelector("#counter_{{ widget.attrs.id}}").innerHTML = this.value.length + '글자';
    })
</script>

"""
class starWidget(forms.TextInput):
    input_type = 'rating'
    template_name = "widgets/star_rate.html"

    class Media:
        css = {
            'all':[
                'widgets/rateit/rateit.css'
            ]
        }
        js = [
            "//code.jquery.com/jquery-3.4.1.min.js",
            'widgets/rateit/jquery.rateit.min.js'
        ]

    def build_attrs(self, *args, **kwargs):
        attrs = super().build_attrs(*args, **kwargs)
        attrs.update({
            'min': 1,
            'max': 5,
            'step': 1,
        })
        return attrs

"""

{% load static %}

{% include "django/forms/widgets/input.html" %}

{{ form.media }}

<div id="star_{{ widget.attrs.id }}" class="rateit" data-rateit-backingfld="#{{ widget.attrs.id }}"></div>

<input type="rating" name="grade" value="4" required="" id="id_grade" min="0" max="5" step="1" style="display: none;">

<div id="star_id_grade" class="rateit rateit-bg" data-rateit-backingfld="#id_grade">
	<!-- 생략 -->
</div>

"""
