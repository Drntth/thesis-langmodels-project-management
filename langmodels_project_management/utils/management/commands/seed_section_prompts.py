from django.core.management.base import BaseCommand
from ai_documentation.models import DocumentSection, DocumentType


class Command(BaseCommand):
    help = "Seed the databse with prompts for sections"

    def handle(self, *args, **kwargs):
        document_types = DocumentType.objects.all()

        if not document_types.exists():
            self.stdout.write(
                self.style.WARNING(
                    "No document types found in the database. Run seed_document_types seeder first!"
                )
            )
            return

        for doc_type in document_types:
            if doc_type.name == "Specification":
                self.seed_specification_sections(doc_type)
            elif doc_type.name == "SRS":
                self.seed_srs_sections(doc_type)
            else:
                self.stdout.write(
                    self.style.WARNING(
                        f"Skipping unknown document type: {doc_type.name}"
                    )
                )

        self.stdout.write(
            self.style.SUCCESS(
                "Successfully seeded document sections for all document types."
            )
        )

    def seed_specification_sections(self, doc_type):
        self.stdout.write(f"Seeding sections for document type: {doc_type.name}")

        sections_data = [
            {
                "title": "## 1. Introduction",
                "prompt": (
                    "Generate an introduction for a project specification document. "
                    "Include details such as project name, version, author, and date. "
                    "Provide a concise overview of the project's background, purpose, and key aspects. "
                    "Maintain a formal and informative tone."
                ),
                "dependencies": [],
            },
            {
                "title": "## 2. Requirements",
                "prompt": (
                    "Generate an overview for the requirements section of a project specification document. "
                    "Provide a summary that sets the context for the detailed sub-sections."
                ),
                "dependencies": ["## 1. Introduction"],
            },
            {
                "title": "### Functional Requirements",
                "prompt": (
                    "Generate a detailed list of functional requirements for a project specification document. "
                    "Present them as bullet points with checkboxes, ensuring clarity and completeness."
                ),
                "dependencies": ["## 2. Requirements"],
            },
            {
                "title": "### Non-Functional Requirements",
                "prompt": (
                    "Generate a detailed list of non-functional requirements for a project specification document. "
                    "Include aspects such as performance, scalability, and security, and use bullet points for clarity."
                ),
                "dependencies": ["### Functional Requirements"],
            },
            {
                "title": "## 3. System Architecture",
                "prompt": (
                    "Generate a system architecture description for a project specification document. "
                    "Describe the overall architecture of the application and provide guidelines for including diagrams or visual representations if necessary. "
                    "Use technical language appropriate for a developer audience."
                ),
                "dependencies": ["## 2. Requirements"],
            },
            {
                "title": "## 4. Data Model",
                "prompt": (
                    "Generate a description for the data model section of a project specification document. "
                    "Explain the database structure, key entities, and their relationships. "
                    "Use clear and precise language suitable for technical readers."
                ),
                "dependencies": ["## 3. System Architecture"],
            },
            {
                "title": "## 5. API Specification",
                "prompt": (
                    "Generate an API specification section for a project specification document. "
                    "Include details such as endpoints, HTTP methods, and a brief description of each API's purpose. "
                    "Present the information in a structured format, for example, using a table layout."
                ),
                "dependencies": ["## 4. Data Model"],
            },
            {
                "title": "## 6. User Interface",
                "prompt": (
                    "Generate a user interface section for a project specification document. "
                    "Describe the overall layout and design of the application, including key UI elements and any available wireframes or design mockups. "
                    "Use descriptive language to clearly illustrate the interface features."
                ),
                "dependencies": ["## 5. API Specification"],
            },
            {
                "title": "## 7. Deployment",
                "prompt": (
                    "Generate a deployment section for a project specification document. "
                    "Outline the steps required to deploy the application, including any dependencies and configuration requirements. "
                    "Use clear, actionable language in your instructions."
                ),
                "dependencies": ["## 6. User Interface"],
            },
            {
                "title": "## 8. Future Enhancements",
                "prompt": (
                    "Generate a future enhancements section for a project specification document. "
                    "Suggest potential improvements, additional features, or extensions that could be implemented in later versions. "
                    "Keep the tone forward-thinking and innovative."
                ),
                "dependencies": ["## 7. Deployment"],
            },
        ]

        section_instances = {}
        for section in sections_data:
            obj, created = DocumentSection.objects.get_or_create(
                document_type=doc_type,
                title=section["title"],
                defaults={"prompt": section["prompt"]},
            )
            section_instances[section["title"]] = obj
            if created:
                self.stdout.write(self.style.SUCCESS(f"Created: {section['title']}"))
            else:
                self.stdout.write(f"Already exists: {section['title']}")

        for section in sections_data:
            current_section = section_instances[section["title"]]
            for dependency_title in section["dependencies"]:
                dep_section = section_instances.get(dependency_title)
                if dep_section:
                    current_section.dependencies.add(dep_section)
                    self.stdout.write(
                        self.style.SUCCESS(
                            f"Set dependency: {section['title']} -> {dependency_title}"
                        )
                    )

        self.stdout.write(
            self.style.SUCCESS(
                "Successfully seeded Specification document sections with prompts and dependencies!"
            )
        )

    def seed_srs_sections(self, doc_type):
        self.stdout.write(f"Seeding SRS sections for document type: {doc_type.name}")

        sections_data = [
            {
                "title": "## 1. Introduction",
                "prompt": (
                    "Generate an introduction for the Software Requirements Specification (SRS) document. "
                    "Provide a brief overview of the document's purpose and structure."
                ),
                "dependencies": [],
            },
            {
                "title": "### 1.1 Purpose",
                "prompt": (
                    "Generate a 'Purpose' section that explains the objective of the SRS document. "
                    "Include why the document is created and what it aims to achieve."
                ),
                "dependencies": ["## 1. Introduction"],
            },
            {
                "title": "### 1.2 Scope",
                "prompt": (
                    "Generate a 'Scope' section that outlines the boundaries of the system, including what the system will and will not do. "
                    "Reference the project's primary goals."
                ),
                "dependencies": ["### 1.1 Purpose"],
            },
            {
                "title": "### 1.3 Definitions, Acronyms, and Abbreviations",
                "prompt": (
                    "Generate a section listing key definitions, acronyms, and abbreviations used throughout the SRS document."
                ),
                "dependencies": ["### 1.2 Scope"],
            },
            {
                "title": "### 1.4 References",
                "prompt": (
                    "Generate a 'References' section that provides a list of relevant documentation, standards, or external sources cited in the SRS document."
                ),
                "dependencies": ["### 1.3 Definitions, Acronyms, and Abbreviations"],
            },
            {
                "title": "### 1.5 Overview",
                "prompt": (
                    "Generate an 'Overview' section that summarizes the structure and contents of the SRS document, highlighting key sections."
                ),
                "dependencies": ["### 1.4 References"],
            },
            {
                "title": "## 2. Overall Description",
                "prompt": (
                    "Generate an 'Overall Description' section that provides a high-level view of the system, including its purpose, context, and major functions."
                ),
                "dependencies": ["## 1. Introduction", "### 1.5 Overview"],
            },
            {
                "title": "### 2.1 Product Perspective",
                "prompt": (
                    "Generate a 'Product Perspective' section that describes how the system fits into the broader context, including integration with external systems or existing infrastructure."
                ),
                "dependencies": ["## 2. Overall Description"],
            },
            {
                "title": "### 2.2 Product Functions",
                "prompt": (
                    "Generate a 'Product Functions' section that outlines the core functionalities of the system, listing main features and capabilities."
                ),
                "dependencies": ["### 2.1 Product Perspective"],
            },
            {
                "title": "### 2.3 User Characteristics",
                "prompt": (
                    "Generate a 'User Characteristics' section that describes the target audience for the system, including user roles and relevant attributes."
                ),
                "dependencies": ["### 2.2 Product Functions"],
            },
            {
                "title": "### 2.4 Constraints",
                "prompt": (
                    "Generate a 'Constraints' section that lists any limitations or restrictions affecting the system, such as technical or regulatory constraints."
                ),
                "dependencies": ["### 2.3 User Characteristics"],
            },
            {
                "title": "### 2.5 Assumptions and Dependencies",
                "prompt": (
                    "Generate an 'Assumptions and Dependencies' section that outlines underlying assumptions and external dependencies impacting the system."
                ),
                "dependencies": ["### 2.4 Constraints", "## 1. Introduction"],
            },
            {
                "title": "## 3. Functional Requirements",
                "prompt": (
                    "Generate a 'Functional Requirements' section that details specific features and functions the system must perform."
                ),
                "dependencies": [
                    "### 2.5 Assumptions and Dependencies",
                    "## 2. Overall Description",
                ],
            },
            {
                "title": "### 3.1 [Feature Name]",
                "prompt": (
                    "Generate a sample functional requirement for a key feature. Include a description, preconditions, and postconditions."
                ),
                "dependencies": ["## 3. Functional Requirements"],
            },
            {
                "title": "### 3.2 [Feature Name]",
                "prompt": (
                    "Generate another sample functional requirement for a different key feature, following a similar structure."
                ),
                "dependencies": ["### 3.1 [Feature Name]"],
            },
            {
                "title": "## 4. External Interface Requirements",
                "prompt": (
                    "Generate an 'External Interface Requirements' section that describes interfaces between the system and external entities, including user interfaces and software/hardware interfaces."
                ),
                "dependencies": ["## 3. Functional Requirements"],
            },
            {
                "title": "### 4.1 User Interfaces",
                "prompt": (
                    "Generate a 'User Interfaces' section that details the design and functionality of the system's user interface."
                ),
                "dependencies": ["## 4. External Interface Requirements"],
            },
            {
                "title": "### 4.2 Software Interfaces",
                "prompt": (
                    "Generate a 'Software Interfaces' section that outlines the interfaces between the system and other software components or external systems."
                ),
                "dependencies": ["### 4.1 User Interfaces"],
            },
            {
                "title": "### 4.3 Hardware Interfaces",
                "prompt": (
                    "Generate a 'Hardware Interfaces' section that specifies the hardware requirements and interfaces related to the system."
                ),
                "dependencies": ["### 4.2 Software Interfaces"],
            },
            {
                "title": "## 5. Non-Functional Requirements",
                "prompt": (
                    "Generate a 'Non-Functional Requirements' section that describes system qualities such as performance, security, scalability, and reliability."
                ),
                "dependencies": ["## 4. External Interface Requirements"],
            },
            {
                "title": "## 6. Appendices",
                "prompt": (
                    "Generate an 'Appendices' section that provides additional information, diagrams, or workflows that support the SRS document."
                ),
                "dependencies": ["## 5. Non-Functional Requirements"],
            },
        ]

        section_instances = {}
        for section in sections_data:
            obj, created = DocumentSection.objects.get_or_create(
                document_type=doc_type,
                title=section["title"],
                defaults={"prompt": section["prompt"]},
            )
            section_instances[section["title"]] = obj
            if created:
                self.stdout.write(self.style.SUCCESS(f"Created: {section['title']}"))
            else:
                self.stdout.write(f"Already exists: {section['title']}")

        for section in sections_data:
            current_section = section_instances[section["title"]]
            for dependency_title in section["dependencies"]:
                dep_section = section_instances.get(dependency_title)
                if dep_section:
                    current_section.dependencies.add(dep_section)
                    self.stdout.write(
                        self.style.SUCCESS(
                            f"Set dependency: {section['title']} -> {dependency_title}"
                        )
                    )

        self.stdout.write(
            self.style.SUCCESS(
                "Successfully seeded SRS document sections with prompts and dependencies!"
            )
        )
