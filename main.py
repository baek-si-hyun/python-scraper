from extractors.wwr import extract_wwr_jobs
from extractors.indeed import extract_indeed_jobs

wwr = extract_wwr_jobs("remote-back-end-programming-jobs")
indeed = extract_indeed_jobs("python")
