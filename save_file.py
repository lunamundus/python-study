import csv

def save_to_file(file_name, jobs):
    job_file = open(f"{file_name}.csv", mode='w', encoding="UTF-8")
    writter = csv.writer(job_file)
    writter.writerow(["Title", "Company", "Language", "Reward", "Link"])

    for job in jobs:
        writter.writerow(job.values())

    job_file.close()