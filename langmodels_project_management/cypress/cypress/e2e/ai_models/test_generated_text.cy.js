describe("Test Generated Text (Guest)", () => {
  beforeEach(() => {
    cy.visit("/ai-models/test-generated-text");
  });

  it("Content", () => {
    cy.get("div.card.shadow-lg.border-secondary.m-2").then($card => {
      if ($card.find("h2.card-title").length) {
        cy.get("h2.card-title").should("contain", "Test Models Generated Text");
        cy.get("p.card-text").contains("Model:").should("exist");
        cy.get("span.badge.bg-secondary").should("exist");
        cy.get("p.card-text").contains("Prompt:").should("exist");
        cy.get("div.card-text.text-secondary").should("exist");
        cy.get("div.card-footer").within(() => {
          cy.get("a.btn").should("contain", "Back to Generation");
        });
      } else {
        cy.get("p.text-muted").should("not.be.empty");
      }
    });
  });

  it("Help & Tips", () => {
    cy.get("div.card").contains("Help & Tips").should("exist");
  });
});

describe("Test Generated Text (User)", () => {
  beforeEach(() => {
    cy.login("user", "userPass123");
    cy.visit("/ai-models/test-generated-text");
  });

  it("Content", () => {
    cy.get("div.card.shadow-lg.border-secondary.m-2").then($card => {
      if ($card.find("h2.card-title").length) {
        cy.get("h2.card-title").should("contain", "Test Models Generated Text");
        cy.get("p.card-text").contains("Model:").should("exist");
        cy.get("span.badge.bg-secondary").should("exist");
        cy.get("p.card-text").contains("Prompt:").should("exist");
        cy.get("div.card-text.text-secondary").should("exist");
        cy.get("div.card-footer").within(() => {
          cy.get("a.btn").should("contain", "Back to Generation");
        });
      } else {
        cy.get("p.text-muted").should("not.be.empty");
      }
    });
  });

  it("Help & Tips", () => {
    cy.get("div.card").contains("Help & Tips").should("exist");
  });
});

describe("Test Generated Text (Staff)", () => {
  beforeEach(() => {
    cy.login("staff", "staffPass123");
    cy.visit("/ai-models/test-generated-text");
  });

  it("Content", () => {
    cy.get("div.card.shadow-lg.border-secondary.m-2").then($card => {
      if ($card.find("h2.card-title").length) {
        cy.get("h2.card-title").should("contain", "Test Models Generated Text");
        cy.get("p.card-text").contains("Model:").should("exist");
        cy.get("span.badge.bg-secondary").should("exist");
        cy.get("p.card-text").contains("Prompt:").should("exist");
        cy.get("div.card-text.text-secondary").should("exist");
        cy.get("div.card-footer").within(() => {
          cy.get("a.btn").should("contain", "Back to Generation");
        });
      } else {
        cy.get("p.text-muted").should("not.be.empty");
      }
    });
  });

  it("Help & Tips", () => {
    cy.get("div.card").contains("Help & Tips").should("exist");
  });
});

describe("Test Generated Text (Superuser)", () => {
  beforeEach(() => {
    cy.login("superuser", "superuserPass123");
    cy.visit("/ai-models/test-generated-text");
  });

  it("Content", () => {
    cy.get("div.card.shadow-lg.border-secondary.m-2").then($card => {
      if ($card.find("h2.card-title").length) {
        cy.get("h2.card-title").should("contain", "Test Models Generated Text");
        cy.get("p.card-text").contains("Model:").should("exist");
        cy.get("span.badge.bg-secondary").should("exist");
        cy.get("p.card-text").contains("Prompt:").should("exist");
        cy.get("div.card-text.text-secondary").should("exist");
        cy.get("div.card-footer").within(() => {
          cy.get("a.btn").should("contain", "Back to Generation");
        });
      } else {
        cy.get("p.text-muted").should("not.be.empty");
      }
    });
  });

  it("Help & Tips", () => {
    cy.get("div.card").contains("Help & Tips").should("exist");
  });
});
