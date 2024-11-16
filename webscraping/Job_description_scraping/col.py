from bs4 import BeautifulSoup


html = '''<section class="styles_job-desc-container__txpYf">
    <div class="">
        <h2>Job description</h2>
    </div>
    <div class="">
        <div class="styles_JDC__dang-inner-html__h0K4t">
            <p> </p>
            <p><strong>Job Description: Senior ML Engineer Join the Innovation at Outnovate</strong></p>
            <p>Are you ready to architect intelligent systems that empower data to see, think, and act? Outnovate is
                seeking a <strong>Senior ML Engineer</strong> to build and deploy impactful machine learning solutions.
                This hybrid role based in <strong>Bangalore</strong> offers the opportunity to leverage advanced tools
                and collaborate across teams to deliver cutting-edge results.</p>
            <p><strong>Role &amp; Responsibilities</strong></p>
            <ul>
                <li><strong>Model Development:</strong> Design and implement production-ready machine learning models
                    with <strong>Python, Spark, and TensorFlow</strong>.</li>
                <li><strong>ML Pipeline Orchestration:</strong> Harmonize ML models with cloud platforms like
                    <strong>AWS</strong> and <strong>GCP</strong>, and MLOps tools like <strong>MLFlow</strong> and
                    <strong>Seldon</strong>.</li>
                <li><strong>Data Processing Expertise:</strong> Handle complex data manipulations with tools like
                    <strong>SQL, Apache Spark, and Hadoop</strong>.</li>
                <li><strong>Collaborative Integration:</strong> Partner with data scientists, engineers, and
                    stakeholders to transform data into actionable insights.</li>
                <li><strong>Microservices Development:</strong> Develop and manage microservices using <strong>Docker
                        and Kubernetes</strong> to ensure smooth deployment and scalability.</li>
            </ul>
        </div>
    </div>
</section>'''

soup = BeautifulSoup(html, 'html.parser')

# Initialize a dictionary to store the headings and their content
job_details = {}

# Find all sections with headings and content
sections = soup.find_all(['h2', 'p', 'ul', 'div'], recursive=True)

current_heading = None

# Extract the headings and their content
for section in sections:
    if section.name == 'h2':  # Detect headings
        current_heading = section.text.strip()
        job_details[current_heading] = []
    elif current_heading:
        # Store content under the current heading
        if section.name in ['p', 'ul']:
            job_details[current_heading].append(section.get_text(strip=True))

# Clean up dictionary
job_details = {k: ' '.join(v).strip() for k, v in job_details.items() if v}

# Display the dictionary
print(job_details)