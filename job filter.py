jobs = [
    {"company": "Language Academy", "role": "English Tutor", "skills": ["english", "portuguese"]},
    {"company": "Braga Tech", "role": "Python Developer", "skills": ["python", "git"]},
    {"company": "Tourist Shop", "role": "Sales Clerk", "skills": ["english", "sales"]},
]

def filter_jobs(user_skills):
    user_skills = [s.lower().strip() for s in user_skills]
    matches = []
    for job in jobs:
        for skill in job["skills"]:
            if skill in user_skills:
                matches.append(job)
                break
    return matches

search = input("Enter skills (comma separated): ").split(",")
results = filter_jobs(search)

if results:
    for job in results:
        print(f"Match: {job['role']} at {job['company']}")
else:
    print("No matches found.")
