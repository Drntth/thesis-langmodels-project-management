describe("Create Document (User)", () => {
  beforeEach(() => {
    cy.login('user', 'userPass123');
    cy.visit('/ai-docs/create');
  });

  it("Title | Header", () => {
    cy.title().should("eq", "Create Document");
    cy.get(".card-title")
      .contains("Create Document")
      .should("be.visible");
  });

  it("Form Fields", () => {
    cy.contains("label", "Title").should("be.visible");
    cy.contains("label", "Content (Template)").should("be.visible");
    cy.contains("label", "Project").should("be.visible");
    cy.contains("label", "Type").should("be.visible");
    cy.contains("label", "Ai Model").should("be.visible");

    cy.get('form[action="/ai-docs/create"]').within(() => {
      cy.get('[name="title"]').should("exist");
      cy.get('[name="content"]').should("exist");
      cy.get('[name="project"]').should("exist");
      cy.get('[name="type"]').should("exist");
      cy.get('[name="ai_model"]').should("exist");
    });
  });

  it("Form Action & CSRF Token", () => {
    cy.get('form[action="/ai-docs/create"]')
      .should("have.attr", "action")
      .and("include", "/ai-docs/create");
    cy.get('form input[name="csrfmiddlewaretoken"]').should("exist");
  });

  it("Cancel | Create Buttons", () => {
    cy.get("a.btn.btn-secondary")
      .contains("Cancel")
      .should("be.visible")
      .and("have.attr", "href")
      .and("include", "ai-docs/list");

    cy.get("button[type='submit']")
      .contains("Create")
      .should("be.visible");
  });

  it("Sidebar Help & Tips", () => {
    cy.get(".card.shadow-lg.border-secondary")
      .contains("Help & Tips")
      .should("be.visible");
    cy.get(".card.shadow-lg.border-secondary")
      .contains("How to Create a Document")
      .should("be.visible");
    cy.get(".card.shadow-lg.border-secondary")
      .contains("Tips for Writing Content")
      .should("be.visible");
    cy.get(".card.shadow-lg.border-secondary")
      .contains("Choosing an AI Model")
      .should("be.visible");
    cy.get(".card.shadow-lg.border-secondary")
      .contains("Important Notes")
      .should("be.visible");
  });
});

describe("Create Document (Staff)", () => {
  beforeEach(() => {
    cy.login('staff', 'staffPass123');
    cy.visit('/ai-docs/create');
  });

  it("Title | Header", () => {
    cy.title().should("eq", "Create Document");
    cy.get(".card-title")
      .contains("Create Document")
      .should("be.visible");
  });

  it("Form Fields", () => {
    cy.contains("label", "Title").should("be.visible");
    cy.contains("label", "Content (Template)").should("be.visible");
    cy.contains("label", "Project").should("be.visible");
    cy.contains("label", "Type").should("be.visible");
    cy.contains("label", "Ai Model").should("be.visible");

    cy.get('form[action="/ai-docs/create"]').within(() => {
      cy.get('[name="title"]').should("exist");
      cy.get('[name="content"]').should("exist");
      cy.get('[name="project"]').should("exist");
      cy.get('[name="type"]').should("exist");
      cy.get('[name="ai_model"]').should("exist");
    });
  });

  it("Form Action & CSRF Token", () => {
    cy.get('form[action="/ai-docs/create"]')
      .should("have.attr", "action")
      .and("include", "/ai-docs/create");
    cy.get('form input[name="csrfmiddlewaretoken"]').should("exist");
  });

  it("Cancel | Create Buttons", () => {
    cy.get("a.btn.btn-secondary")
      .contains("Cancel")
      .should("be.visible")
      .and("have.attr", "href")
      .and("include", "ai-docs/list");

    cy.get("button[type='submit']")
      .contains("Create")
      .should("be.visible");
  });

  it("Sidebar Help & Tips", () => {
    cy.get(".card.shadow-lg.border-secondary")
      .contains("Help & Tips")
      .should("be.visible");
    cy.get(".card.shadow-lg.border-secondary")
      .contains("How to Create a Document")
      .should("be.visible");
    cy.get(".card.shadow-lg.border-secondary")
      .contains("Tips for Writing Content")
      .should("be.visible");
    cy.get(".card.shadow-lg.border-secondary")
      .contains("Choosing an AI Model")
      .should("be.visible");
    cy.get(".card.shadow-lg.border-secondary")
      .contains("Important Notes")
      .should("be.visible");
  });
});

describe("Create Document (Superuser)", () => {
  beforeEach(() => {
    cy.login('superuser', 'superuserPass123');
    cy.visit('/ai-docs/create');
  });

  it("Title | Header", () => {
    cy.title().should("eq", "Create Document");
    cy.get(".card-title")
      .contains("Create Document")
      .should("be.visible");
  });

  it("Form Fields", () => {
    cy.contains("label", "Title").should("be.visible");
    cy.contains("label", "Content (Template)").should("be.visible");
    cy.contains("label", "Project").should("be.visible");
    cy.contains("label", "Type").should("be.visible");
    cy.contains("label", "Ai Model").should("be.visible");

    cy.get('form[action="/ai-docs/create"]').within(() => {
      cy.get('[name="title"]').should("exist");
      cy.get('[name="content"]').should("exist");
      cy.get('[name="project"]').should("exist");
      cy.get('[name="type"]').should("exist");
      cy.get('[name="ai_model"]').should("exist");
    });
  });

  it("Form Action & CSRF Token", () => {
    cy.get('form[action="/ai-docs/create"]')
      .should("have.attr", "action")
      .and("include", "/ai-docs/create");
    cy.get('form input[name="csrfmiddlewaretoken"]').should("exist");
  });

  it("Cancel | Create Buttons", () => {
    cy.get("a.btn.btn-secondary")
      .contains("Cancel")
      .should("be.visible")
      .and("have.attr", "href")
      .and("include", "ai-docs/list");

    cy.get("button[type='submit']")
      .contains("Create")
      .should("be.visible");
  });

  it("Sidebar Help & Tips", () => {
    cy.get(".card.shadow-lg.border-secondary")
      .contains("Help & Tips")
      .should("be.visible");
    cy.get(".card.shadow-lg.border-secondary")
      .contains("How to Create a Document")
      .should("be.visible");
    cy.get(".card.shadow-lg.border-secondary")
      .contains("Tips for Writing Content")
      .should("be.visible");
    cy.get(".card.shadow-lg.border-secondary")
      .contains("Choosing an AI Model")
      .should("be.visible");
    cy.get(".card.shadow-lg.border-secondary")
      .contains("Important Notes")
      .should("be.visible");
  });
});
