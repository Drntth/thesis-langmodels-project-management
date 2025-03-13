describe("Test Models (Guest)", () => {
  beforeEach(() => {
    cy.visit("/ai-models/test-models");
  });

  it("Title", () => {
    cy.get("h2.card-title").should("contain", "Test Models");
  });

  it("Form", () => {
    cy.get("form").within(() => {
      cy.contains("label", "AI Model").should("exist");
      cy.contains("label", "Prompt").should("exist");
      cy.get("input[name='csrfmiddlewaretoken']").should("exist");
      cy.get(".input-group").should("have.length.at.least", 2);
      cy.get("button[type='submit']").should("contain", "Generate");
    });
  });

  it("Help & Tips", () => {
    cy.get("div.card").contains("Help & Tips").should("exist");
  });
});

describe("Test Models (User)", () => {
  beforeEach(() => {
    cy.login("user", "userPass123");
    cy.visit("/ai-models/test-models");
  });

  it("Title", () => {
    cy.get("h2.card-title").should("contain", "Test Models");
  });

  it("Form", () => {
    cy.get('form[action="/ai-models/test-models"]').within(() => {
      cy.contains("label", "AI Model").should("exist");
      cy.contains("label", "Prompt").should("exist");
      cy.get("input[name='csrfmiddlewaretoken']").should("exist");
      cy.get(".input-group").should("have.length.at.least", 2);
      cy.get("button[type='submit']").should("contain", "Generate");
    });
  });

  it("Help & Tips", () => {
    cy.get("div.card").contains("Help & Tips").should("exist");
  });
});

describe("Test Models (Staff)", () => {
  beforeEach(() => {
    cy.login("staff", "staffPass123");
    cy.visit("/ai-models/test-models");
  });

  it("Title", () => {
    cy.get("h2.card-title").should("contain", "Test Models");
  });

  it("Form", () => {
    cy.get('form[action="/ai-models/test-models"]').within(() => {
      cy.contains("label", "AI Model").should("exist");
      cy.contains("label", "Prompt").should("exist");
      cy.get("input[name='csrfmiddlewaretoken']").should("exist");
      cy.get(".input-group").should("have.length.at.least", 2);
      cy.get("button[type='submit']").should("contain", "Generate");
    });
  });

  it("Help & Tips", () => {
    cy.get("div.card").contains("Help & Tips").should("exist");
  });
});

describe("Test Models (Superuser)", () => {
  beforeEach(() => {
    cy.login("superuser", "superuserPass123");
    cy.visit("/ai-models/test-models");
  });

  it("Title", () => {
    cy.get("h2.card-title").should("contain", "Test Models");
  });

  it("Form", () => {
    cy.get('form[action="/ai-models/test-models"]').within(() => {
      cy.contains("label", "AI Model").should("exist");
      cy.contains("label", "Prompt").should("exist");
      cy.get("input[name='csrfmiddlewaretoken']").should("exist");
      cy.get(".input-group").should("have.length.at.least", 2);
      cy.get("button[type='submit']").should("contain", "Generate");
    });
  });

  it("Help & Tips", () => {
    cy.get("div.card").contains("Help & Tips").should("exist");
  });
});
