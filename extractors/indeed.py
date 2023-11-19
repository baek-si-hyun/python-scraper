from bs4 import BeautifulSoup
from requests import get

def get_page_count(keyword):
  base_url = "https://kr.indeed.com/jobs"
  response = get(f"{base_url}?q={keyword}")

  if response.status_code != 200:
    print("페이지를 찾을수 없습니다.")
  else:
    soup = BeautifulSoup(response.text, "html.parser")
    pagination = soup.find("ul", class_="pagination-list")
    if pagination is None:
      return 1
    pages = pagination.find_all("li", recursive=False)
    count = len(pages)
    if count >= 5:
      return 5
    else:
      return count

get_page_count("python")


def extract_indeed_jobs(keyword):
  pages = get_page_count(keyword)
  results = []
  for page in range(pages):
    base_url = "https://kr.indeed.com/jobs"
    final_url = f"{base_url}?q={keyword}&start={page*10}"
    response = get(final_url)

    if response.status_code != 200:
      print("페이지를 찾을수 없습니다.")
    else:
      soup = BeautifulSoup(response.text, "html.parser")
      job_list = soup.find("ul", class_="jobsearch-ResultsList")
      jobs = job_list.find_all("li", recursive=False)
      for job in jobs:
        zone = job.find("div", class_="mosaic-zone")
        if zone is None:
          anchor = job.select_one("h2 a")
          title = anchor['aria-label']
          link = anchor['href']
          company = job.find("span", class_="companyName")
          location = job.find("div", class_="companyLocation")
          job_data = {
              'link': f"https://kr.indeed.com{link}",
              'company': company.string,
              'location': location.string,
              'position': title.string
          }
          results.append(job_data)
  return results

jobs = extract_indeed_jobs("python")
print(jobs)