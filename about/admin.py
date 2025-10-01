from django.contrib import admin
from django.core.exceptions import ValidationError
from django import forms
from .models import About, Team, SocialMedia, TeamSocialMedia, Contact, Slider, Gallery, Video, Testimonial

class SliderAdminForm(forms.ModelForm):
    class Meta:
        model = Slider
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        action = cleaned_data.get('action')
        action_text = cleaned_data.get('action_text')
        
        if action and action != 'none' and not action_text:
            raise ValidationError('Action text is required when an action is selected')
        return cleaned_data

@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    form = SliderAdminForm
    list_display = ('title', 'subtitle', 'action', 'active', 'created_at')
    list_filter = ('active', 'action')
    search_fields = ('title', 'subtitle')
    readonly_fields = ('created_at', 'updated_at')
    
    def save_model(self, request, obj, form, change):
        try:
            super().save_model(request, obj, form, change)
        except Exception as e:
            print(f"Error in SliderAdmin save_model: {str(e)}")
            raise

# Register other models
admin.site.register(About)
admin.site.register(Team)
admin.site.register(SocialMedia)
admin.site.register(TeamSocialMedia)
# admin.site.register(Contact)
admin.site.register(Gallery)
admin.site.register(Video)
admin.site.register(Testimonial)