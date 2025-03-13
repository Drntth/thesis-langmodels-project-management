describe("Generate (User)", () => {
  beforeEach(() => {
    cy.login("user", "userPass123");
    cy.visit("/ai-models/generate");
  });

  it("Document content", () => {
    cy.get("div.card.shadow-lg.border-dark.m-2").then($container => {
      if ($container.text().includes("No document found.")) {
        cy.contains("No document found.").should("exist");
      } else {
        cy.get("div.card-header.bg-dark.text-light.shadow-lg.d-flex").should("exist");
        cy.get("h2.card-title").should("not.be.empty");
        cy.contains("Project Description").should("exist");
        cy.get("p.card-text").should("not.be.empty");
        cy.get("form").each($form => {
          cy.wrap($form).within(() => {
            cy.get("h4").should("not.be.empty");
            cy.get("input[type='hidden'][name='section_title']").should("exist");
            cy.get("textarea[name='section_content']").should("exist");
            cy.contains("Generate").should("exist");
            cy.contains("Save").should("exist");
          });
        });
        cy.contains("Back to Document Details").should("exist");
      }
    });
  });

  it("Sidebar Help & Tips", () => {
    cy.get("div.card").contains("Help & Tips").should("exist");
  });
});

describe("Generate (Staff)", () => {
  beforeEach(() => {
    cy.login("staff", "staffPass123");
    cy.visit("/ai-models/generate");
  });

  it("Document content", () => {
    cy.get("div.card.shadow-lg.border-dark.m-2").then($container => {
      if ($container.text().includes("No document found.")) {
        cy.contains("No document found.").should("exist");
      } else {
        cy.get("div.card-header.bg-dark.text-light.shadow-lg.d-flex").should("exist");
        cy.get("h2.card-title").should("not.be.empty");
        cy.contains("Project Description").should("exist");
        cy.get("p.card-text").should("not.be.empty");
        cy.get("form").each($form => {
          cy.wrap($form).within(() => {
            cy.get("h4").should("not.be.empty");
            cy.get("input[type='hidden'][name='section_title']").should("exist");
            cy.get("textarea[name='section_content']").should("exist");
            cy.contains("Generate").should("exist");
            cy.contains("Save").should("exist");
          });
        });
        cy.contains("Back to Document Details").should("exist");
      }
    });
  });

  it("Sidebar Help & Tips", () => {
    cy.get("div.card").contains("Help & Tips").should("exist");
  });
});

describe("Generate (Superuser)", () => {
  beforeEach(() => {
    cy.login("superuser", "superuserPass123");
    cy.visit("/ai-models/generate");
  });

  it("Document content", () => {
    cy.get("div.card.shadow-lg.border-dark.m-2").then($container => {
      if ($container.text().includes("No document found.")) {
        cy.contains("No document found.").should("exist");
      } else {
        cy.get("div.card-header.bg-dark.text-light.shadow-lg.d-flex").should("exist");
        cy.get("h2.card-title").should("not.be.empty");
        cy.contains("Project Description").should("exist");
        cy.get("p.card-text").should("not.be.empty");
        cy.get("form").each($form => {
          cy.wrap($form).within(() => {
            cy.get("h4").should("not.be.empty");
            cy.get("input[type='hidden'][name='section_title']").should("exist");
            cy.get("textarea[name='section_content']").should("exist");
            cy.contains("Generate").should("exist");
            cy.contains("Save").should("exist");
          });
        });
        cy.contains("Back to Document Details").should("exist");
      }
    });
  });

  it("Sidebar Help & Tips", () => {
    cy.get("div.card").contains("Help & Tips").should("exist");
  });
});