from django.shortcuts import render
from myapp1.models import Worker

# Create your views here.
def index_page(request):
    new_worker = Worker(name = "Владимир", second_name = "Петров", salary = 30000)
    new_worker.save()
    # worker_to_change = Worker.objects.get (id = 6).delete()
    # worker_to_change.second_name = 'Задерищенский'
    # worker_to_change.name = 'Василий'
    # worker_to_change.save()
    # print(worker_to_change)

    all_workers = Worker.objects.all()
    print(all_workers)
    
    # salary_warkers = Worker.objects.filter(salary=50000)
    # print(salary_warkers)
    
    for i in all_workers:
        print (f"Фамилия: {i.second_name}, Имя: {i.name}, Зарплата: {i.salary}', ID: {i.id}")

    return render(request, 'index.html')
    


# def about_page(request):
#     return render(request, 'about.html')    