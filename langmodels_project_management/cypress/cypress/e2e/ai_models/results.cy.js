describe("Results (User)", () => {
  beforeEach(() => {
    cy.login("user", "userPass123");
    cy.visit("/ai-models/results");
  });

  it("Content", () => {
    cy.get("div.card.shadow-lg.border-secondary.m-2").then($container => {
      if ($container.find("h2.card-title").length > 0) {
        cy.get("h2.card-title").should("contain", "Results");
        cy.get("div.card-body").within(() => {
          cy.get("p.card-text").should("exist");
          cy.get("p.card-text").then($p => {
            expect($p.text()).to.match(/(Title:|Description:)/);
          });
          cy.get("div.row").within(() => {
            cy.get("div.col-12").each($col => {
              cy.wrap($col).find("div.card.shadow-sm.mb-4").should("exist");
              cy.wrap($col).find("div.card-header").within(() => {
                cy.get("span.badge.bg-secondary").should("exist");
              });
              cy.wrap($col).find("div.card-body").within(() => {
                cy.contains("Generated text").should("exist");
                cy.get("div.card-text").should("exist");
              });
            });
          });
        });
        cy.get("div.card-footer").within(() => {
          cy.contains("Back to Description Generation").should("exist");
          cy.contains("Back to Title Generation").should("exist");
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

describe("Results (Staff)", () => {
  beforeEach(() => {
    cy.login("staff", "staffPass123");
    cy.visit("/ai-models/results");
  });

  it("Content", () => {
    cy.get("div.card.shadow-lg.border-secondary.m-2").then($container => {
      if ($container.find("h2.card-title").length > 0) {
        cy.get("h2.card-title").should("contain", "Results");
        cy.get("div.card-body").within(() => {
          cy.get("p.card-text").should("exist");
          cy.get("p.card-text").then($p => {
            expect($p.text()).to.match(/(Title:|Description:)/);
          });
          cy.get("div.row").within(() => {
            cy.get("div.col-12").each($col => {
              cy.wrap($col).find("div.card.shadow-sm.mb-4").should("exist");
              cy.wrap($col).find("div.card-header").within(() => {
                cy.get("span.badge.bg-secondary").should("exist");
              });
              cy.wrap($col).find("div.card-body").within(() => {
                cy.contains("Generated text").should("exist");
                cy.get("div.card-text").should("exist");
              });
            });
          });
        });
        cy.get("div.card-footer").within(() => {
          cy.contains("Back to Description Generation").should("exist");
          cy.contains("Back to Title Generation").should("exist");
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

describe("Results (Superuser)", () => {
  beforeEach(() => {
    cy.login("superuser", "superuserPass123");
    cy.visit("/ai-models/results");
  });

  it("Content", () => {
    cy.get("div.card.shadow-lg.border-secondary.m-2").then($container => {
      if ($container.find("h2.card-title").length > 0) {
        cy.get("h2.card-title").should("contain", "Results");
        cy.get("div.card-body").within(() => {
          cy.get("p.card-text").should("exist");
          cy.get("p.card-text").then($p => {
            expect($p.text()).to.match(/(Title:|Description:)/);
          });
          cy.get("div.row").within(() => {
            cy.get("div.col-12").each($col => {
              cy.wrap($col).find("div.card.shadow-sm.mb-4").should("exist");
              cy.wrap($col).find("div.card-header").within(() => {
                cy.get("span.badge.bg-secondary").should("exist");
              });
              cy.wrap($col).find("div.card-body").within(() => {
                cy.contains("Generated text").should("exist");
                cy.get("div.card-text").should("exist");
              });
            });
          });
        });
        cy.get("div.card-footer").within(() => {
          cy.contains("Back to Description Generation").should("exist");
          cy.contains("Back to Title Generation").should("exist");
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