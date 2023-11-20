from extractors.wwr import extract_wwr_jobs
from extractors.indeed import extract_indeed_jobs
from file import save_to_file

keyword = input("어떤 언어로 개발하는 직업을 검색하고 싶으신가요?")

wwr = extract_wwr_jobs("remote-back-end-programming-jobs")
indeed = extract_indeed_jobs("python")
jobs = indeed + wwr

save_to_file(keyword, jobs)
