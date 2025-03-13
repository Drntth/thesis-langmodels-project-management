describe("Select Project (User)", () => {
  beforeEach(() => {
    cy.login("user", "userPass123");
    cy.visit("/ai-models/select-project");
  });

  it("Title", () => {
    cy.get("h2.card-title").should("contain", "Select Project");
  });

  it("Form", () => {
    cy.get('form[action="/ai-models/select-project"]').within(() => {
      cy.contains("label", "Project").should("exist");
      cy.get("input[name='csrfmiddlewaretoken']").should("exist");
      cy.get(".input-group").should("exist");
      cy.get("a.btn").should("contain", "Cancel");
      cy.get("button[type='submit']").should("contain", "Select");
    });
  });

  it("Help & Tips", () => {
    cy.get("div.card").contains("Help & Tips").should("exist");
  });
});

describe("Select Project (Staff)", () => {
  beforeEach(() => {
    cy.login("staff", "staffPass123");
    cy.visit("/ai-models/select-project");
  });

  it("Title", () => {
    cy.get("h2.card-title").should("contain", "Select Project");
  });

  it("Form", () => {
    cy.get('form[action="/ai-models/select-project"]').within(() => {
      cy.contains("label", "Project").should("exist");
      cy.get("input[name='csrfmiddlewaretoken']").should("exist");
      cy.get(".input-group").should("exist");
      cy.get("a.btn").should("contain", "Cancel");
      cy.get("button[type='submit']").should("contain", "Select");
    });
  });

  it("Help & Tips", () => {
    cy.get("div.card").contains("Help & Tips").should("exist");
  });
});

describe("Select Project (Superuser)", () => {
  beforeEach(() => {
    cy.login("superuser", "superuserPass123");
    cy.visit("/ai-models/select-project");
  });

  it("Title", () => {
    cy.get("h2.card-title").should("contain", "Select Project");
  });

  it("Form", () => {
    cy.get('form[action="/ai-models/select-project"]').within(() => {
      cy.contains("label", "Project").should("exist");
      cy.get("input[name='csrfmiddlewaretoken']").should("exist");
      cy.get(".input-group").should("exist");
      cy.get("a.btn").should("contain", "Cancel");
      cy.get("button[type='submit']").should("contain", "Select");
    });
  });

  it("Help & Tips", () => {
    cy.get("div.card").contains("Help & Tips").should("exist");
  });
});