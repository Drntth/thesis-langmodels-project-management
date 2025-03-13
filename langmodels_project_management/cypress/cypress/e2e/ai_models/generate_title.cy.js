describe("Generate Title (Guest)", () => {
  beforeEach(() => {
    cy.visit("/ai-models/generate-title");
  });

  it("Title", () => {
    cy.get("h2.card-title").should("contain", "Generate Title");
  });

  it("Form", () => {
    cy.get("form").within(() => {
      cy.contains("label", "Description").should("exist");
      cy.get("input[name='csrfmiddlewaretoken']").should("exist");
      cy.get("input").first().should("exist");
      cy.get("button[type='submit']").should("contain", "Generate");
    });
  });

  it("Help & Tips sidebar", () => {
    cy.get("div.card").contains("Help & Tips").should("exist");
  });
});

describe("Generate Title (User)", () => {
  beforeEach(() => {
    cy.login('user', 'userPass123')
    cy.visit("/ai-models/generate-title");
  });

  it("Title", () => {
    cy.get("h2.card-title").should("contain", "Generate Title");
  });

  it("Form", () => {
    cy.get('form[action="/ai-models/generate-title"]').within(() => {
      cy.contains("label", "Description").should("exist");
      cy.get("input[name='csrfmiddlewaretoken']").should("exist");
      cy.get("input").first().should("exist");
      cy.get("button[type='submit']").should("contain", "Generate");
    });
  });

  it("Help & Tips sidebar", () => {
    cy.get("div.card").contains("Help & Tips").should("exist");
  });
});

describe("Generate Description (Staff)", () => {
  beforeEach(() => {
    cy.login('staff', 'staffPass123')
    cy.visit("/ai-models/generate-description");
  });

  it("Title", () => {
    cy.get("h2.card-title").should("contain", "Generate Description");
  });

  it("Form", () => {
    cy.get('form[action="/ai-models/generate-description"]').within(() => {
      cy.contains("label", "Title").should("exist");
      cy.get("input[name='csrfmiddlewaretoken']").should("exist");
      cy.get("input").first().should("exist");
      cy.get("button[type='submit']").should("contain", "Generate");
    });
  });

  it("Help & Tips sidebar", () => {
    cy.get("div.card").contains("Help & Tips").should("exist");
  });
});

describe("Generate Description (Superuser)", () => {
  beforeEach(() => {
    cy.login('superuser', 'superuserPass123')
    cy.visit("/ai-models/generate-title");
  });

  it("Title", () => {
    cy.get("h2.card-title").should("contain", "Generate Title");
  });

  it("Form", () => {
    cy.get('form[action="/ai-models/generate-title"]').within(() => {
      cy.contains("label", "Description").should("exist");
      cy.get("input[name='csrfmiddlewaretoken']").should("exist");
      cy.get("input").first().should("exist");
      cy.get("button[type='submit']").should("contain", "Generate");
    });
  });

  it("Help & Tips sidebar", () => {
    cy.get("div.card").contains("Help & Tips").should("exist");
  });
});