from django.shortcuts import render, redirect
from .models import Subject, ExamScore
from .forms import SubjectForm, ExamScoreForm


from django.shortcuts import render
from .models import Subject, ExamScore

def home(request):
    subjects = Subject.objects.all()
    charts_data = []

    for subject in subjects:
        scores = ExamScore.objects.filter(subject=subject).order_by('date')
        scores_data = [score.score for score in scores]
        dates_data = [score.date.strftime('%Y-%m-%d') for score in scores]

        # Ensure we are creating pairs of date and score
        dates_scores_pairs = list(zip(dates_data, scores_data))

        charts_data.append({
            'subject': subject.name,
            'dates_scores_pairs': dates_scores_pairs,
            'scores_data': scores_data,
            'dates_data': dates_data
        })

    return render(request, 'tracker/home.html', {
        'subjects': subjects,
        'charts_data': charts_data
    })




def add_subject(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SubjectForm()
    return render(request, 'tracker/add_subject.html', {'form': form})

from django.shortcuts import render, redirect
from .forms import ExamScoreForm

def add_exam_score(request):
    if request.method == 'POST':
        form = ExamScoreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to the home page after saving
    else:
        form = ExamScoreForm()

    return render(request, 'tracker/add_exam_score.html', {'form': form})


def subject_detail(request, subject_id):
    subject = Subject.objects.get(id=subject_id)
    scores = ExamScore.objects.filter(subject=subject).order_by('date')

    # Extract scores and dates for chart
    scores_data = [score.score for score in scores]
    dates_data = [score.date.strftime('%Y-%m-%d') for score in scores]

    context = {
        'subject': subject,
        'scores': scores,
        'scores_data': scores_data,
        'dates_data': dates_data
    }
    
    return render(request, 'tracker/subject_detail.html', context)
