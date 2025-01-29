from django import forms

class ReviewForm(forms.Form):
    user_name = forms.CharField(label="Name:", required=False, max_length=100, error_messages={
        "required": "Your name mustn't be empty (╥﹏╥)",
        "max_length":"Please enter a shorter name (╥﹏╥)"
    })

    review_text = forms.CharField(label="Your feedback", required=False, widget=forms.Textarea, max_length=200)
    rating = forms.IntegerField(label="Your rating", required=False, min_value=1, max_value=5)