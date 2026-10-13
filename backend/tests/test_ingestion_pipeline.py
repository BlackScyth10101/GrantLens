import fitz
import requests

# 1. Create a dummy solicitation PDF
doc_sol = fitz.open()
page_sol = doc_sol.new_page()
page_sol.insert_text((72, 72), "NSF 24-500: Advanced Computing Infrastructure Solicitation\n\nPage limit: 15 pages.\nMinimum font size: 10 pt Arial or 11 pt Times.\nMinimum margins: 1.0 inch.")
sol_bytes = doc_sol.tobytes()

# 2. Create a dummy draft proposal PDF with references, budget section, tables
doc_prop = fitz.open()
page_prop = doc_prop.new_page()
page_prop.insert_text((72, 72), "SCALABLE QUANTUM COMPUTING IN DIAMOND NV CENTERS\n\nPROJECT DESCRIPTION\n\nWe propose an innovative architecture...")
page_prop.insert_text((72, 300), "BUDGET JUSTIFICATION\n\nCategory\tAmount\nPersonnel - PI Salary\t$125,000.00\nPostdoctoral Scholar\t$70,000.00\nEquipment - Cryostat\t$150,000.00\nTotal Direct Costs\t$345,000.00")
page_prop.insert_text((72, 500), "REFERENCES CITED\n\n[1] Smith et al., Quantum 2024.")
prop_bytes = doc_prop.tobytes()

# 3. Login to get token
login_res = requests.post("http://127.0.0.1:8000/api/v1/auth/login", json={
    "email": "sarah.lin@berkeley.edu",
    "password": "ResearchSecurity2026!"
})
token = login_res.json()["access_token"]

# 4. Upload submission
files = {
    "solicitation_file": ("solicitation.pdf", sol_bytes, "application/pdf"),
    "proposal_file": ("proposal.pdf", prop_bytes, "application/pdf")
}
data = {
    "title": "Scalable Quantum Computing in Diamond NV Centers",
    "funding_agency": "NSF 24-500"
}
headers = {"Authorization": f"Bearer {token}"}

upload_res = requests.post("http://127.0.0.1:8000/api/v1/submissions/upload", data=data, files=files, headers=headers)
print("Upload Status Code:", upload_res.status_code)
resp_json = upload_res.json()
print("Submission ID:", resp_json.get("submission_id"))
print("Audit Score:", resp_json.get("audit_score"))
print("Findings Count:", resp_json.get("findings_count"))
for finding in resp_json.get("findings", []):
    print(f" - [{finding['severity']}] {finding['category']}: {finding['message']}")
