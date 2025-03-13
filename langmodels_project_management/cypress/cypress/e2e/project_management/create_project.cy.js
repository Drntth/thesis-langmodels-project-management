describe("Create Project (User)", () => {
  beforeEach(() => {
    cy.login('user', 'userPass123');
    cy.visit('/projects/create');
  });

  it("Title | Header", () => {
    cy.title().should("eq", "Create Project");
    cy.get(".card-title")
      .contains("Create Project")
      .should("be.visible");
  });

  it("Form Fields", () => {
    cy.get('input[name="name"]').should("exist");
    cy.get('[name="description"]').should("exist");
    cy.get('input[name="deadline"]').should("exist");
  });

  it("Form Action & CSRF Token", () => {
    cy.get('form[action="/projects/create"]')
      .should("have.attr", "action")
      .and("include", "/projects/create");
    cy.get('input[name="csrfmiddlewaretoken"]').should("exist");
  });

  it("Cancel | Create Buttons", () => {
    cy.get("a.btn.btn-secondary")
      .contains("Cancel")
      .should("be.visible")
      .and("have.attr", "href")
      .and("include", "projects/list");
    cy.get("button[type='submit']")
      .contains("Create")
      .should("be.visible");
  });

  it("Sidebar Help & Tips", () => {
    cy.get(".card.shadow-lg.border-secondary")
      .contains("Help & Tips")
      .should("be.visible");
    cy.get(".card.shadow-lg.border-secondary")
      .contains("How to Fill Out the Form")
      .should("be.visible");
    cy.get(".card.shadow-lg.border-secondary")
      .contains("Project Name Tips")
      .should("be.visible");
    cy.get(".card.shadow-lg.border-secondary")
      .contains("Description Tips")
      .should("be.visible");
    cy.get(".card.shadow-lg.border-secondary")
      .contains("Deadline Tips")
      .should("be.visible");
  });
});

describe("Create Project (Staff)", () => {
  beforeEach(() => {
    cy.login('staff', 'staffPass123');
    cy.visit('/projects/create');
  });

  it("Title | Header", () => {
    cy.title().should("eq", "Create Project");
    cy.get(".card-title")
      .contains("Create Project")
      .should("be.visible");
  });

  it("Form Fields", () => {
    cy.get('input[name="name"]').should("exist");
    cy.get('[name="description"]').should("exist");
    cy.get('input[name="deadline"]').should("exist");
  });

  it("Form Action & CSRF Token", () => {
    cy.get('form[action="/projects/create"]')
      .should("have.attr", "action")
      .and("include", "/projects/create");
    cy.get('input[name="csrfmiddlewaretoken"]').should("exist");
  });

  it("Cancel | Create Buttons", () => {
    cy.get("a.btn.btn-secondary")
      .contains("Cancel")
      .should("be.visible")
      .and("have.attr", "href")
      .and("include", "projects/list");
    cy.get("button[type='submit']")
      .contains("Create")
      .should("be.visible");
  });

  it("Sidebar Help & Tips", () => {
    cy.get(".card.shadow-lg.border-secondary")
      .contains("Help & Tips")
      .should("be.visible");
    cy.get(".card.shadow-lg.border-secondary")
      .contains("How to Fill Out the Form")
      .should("be.visible");
    cy.get(".card.shadow-lg.border-secondary")
      .contains("Project Name Tips")
      .should("be.visible");
    cy.get(".card.shadow-lg.border-secondary")
      .contains("Description Tips")
      .should("be.visible");
    cy.get(".card.shadow-lg.border-secondary")
      .contains("Deadline Tips")
      .should("be.visible");
  });
});

describe("Create Project (Superuser)", () => {
  beforeEach(() => {
    cy.login('superuser', 'superuserPass123');
    cy.visit('/projects/create');
  });

  it("Title | Header", () => {
    cy.title().should("eq", "Create Project");
    cy.get(".card-title")
      .contains("Create Project")
      .should("be.visible");
  });

  it("Form Fields", () => {
    cy.get('input[name="name"]').should("exist");
    cy.get('[name="description"]').should("exist");
    cy.get('input[name="deadline"]').should("exist");
  });

  it("Form Action & CSRF Token", () => {
    cy.get('form[action="/projects/create"]')
      .should("have.attr", "action")
      .and("include", "/projects/create");
    cy.get('input[name="csrfmiddlewaretoken"]').should("exist");
  });

  it("Cancel | Create Buttons", () => {
    cy.get("a.btn.btn-secondary")
      .contains("Cancel")
      .should("be.visible")
      .and("have.attr", "href")
      .and("include", "projects/list");
    cy.get("button[type='submit']")
      .contains("Create")
      .should("be.visible");
  });

  it("Sidebar Help & Tips", () => {
    cy.get(".card.shadow-lg.border-secondary")
      .contains("Help & Tips")
      .should("be.visible");
    cy.get(".card.shadow-lg.border-secondary")
      .contains("How to Fill Out the Form")
      .should("be.visible");
    cy.get(".card.shadow-lg.border-secondary")
      .contains("Project Name Tips")
      .should("be.visible");
    cy.get(".card.shadow-lg.border-secondary")
      .contains("Description Tips")
      .should("be.visible");
    cy.get(".card.shadow-lg.border-secondary")
      .contains("Deadline Tips")
      .should("be.visible");
  });
});
