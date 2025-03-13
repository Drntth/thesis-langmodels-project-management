describe("Base (Guest)", () => {
  beforeEach(() => {
    cy.visit("/");
  });

  it("Main page title", () => {
    cy.get("h1.display-5").should("be.visible").and("not.be.empty");
  });

  it("Navigation bar", () => {
    cy.get("header").should("be.visible");
    cy.get("header nav").should("exist");
    cy.get("header nav").within(() => {
      cy.contains("Login").should("be.visible");
      cy.contains("Register").should("be.visible");
    });
  });

  it("Footer", () => {
    cy.get("footer").should("be.visible");
  });

  it("User Info", () => {
    cy.contains(".card-header", "User Info").should("be.visible");

    cy.get(".card")
      .contains("span.badge", "Guest")
      .should("be.visible");

    cy.get("#profile-picture").should(
      "have.attr",
      "src",
      "/static/images/default_user.svg"
    );
  });

  it("Quick Actions", () => {
    cy.contains("Quick Actions").should("not.exist");
  });

  it("Main content", () => {
    cy.get("main.container-fluid").should("exist");
  });
});

describe("Base (User)", () => {
  beforeEach(() => {
    cy.login('user', 'userPass123')
    cy.visit('/')
  })

  it("Main page title", () => {
    cy.get("h1.display-5").should("be.visible").and("not.be.empty");
  });

  it("Navigation bar", () => {
    cy.get("header").should("be.visible");
    cy.get("header nav").should("exist");
    cy.get("header nav").find("a").should("have.length.greaterThan", 0);
  });

  it("User info section", () => {
    cy.get(".card-header").contains("User Info").should("be.visible");

    cy.get("#profile-picture").should("be.visible").and(($img) => {
      expect($img.attr("src")).to.match(/\/static\/images\/default_(superuser|staff|user)\.svg/);
      expect($img.attr("src")).to.include("default_user.svg");
    });

    cy.get(".card-body a")
      .first()
      .within(() => {
        cy.get("span.badge").should("contain.text", "user");
      });
  });

  it("Profile link", () => {
    cy.get(".card-body a").first().click();
    cy.url().should("include", "/users/profile");
    cy.visit('/')
  });

  it("User role", () => {
    cy.get(".card-body")
      .first()
      .within(() => {
        cy.get("span.badge").contains("Normal User").should("be.visible");
      });
  });

  it("Quick actions", () => {
    cy.contains('.card-header', 'Quick Actions').parent().within(() => {
      cy.get(".card-body a.btn-outline-dark")
        .should("contain.text", "View My Projects")
        .and("have.attr", "href").and("not.be.empty");

      cy.get(".card-body a.btn-outline-primary")
        .should("contain.text", "View My Documents")
        .and("have.attr", "href").and("not.be.empty");

        cy.get('a.btn-outline-success')
        .should('contain.text', 'Generate Content')
        .and('have.attr', 'href').and('not.be.empty');

      cy.get(".card-body a.btn-outline-danger")
        .should("contain.text", "Test AI Models")
        .and("have.attr", "href").and("not.be.empty");

      cy.get(".card-body a.btn-outline-warning")
        .should("contain.text", "Generate Description")
        .and("have.attr", "href").and("not.be.empty");

      cy.get(".card-body a.btn-outline-info")
        .should("contain.text", "Generate Title")
        .and("have.attr", "href").and("not.be.empty");
      });
  });

  it("Quick action navigation", () => {
    cy.get(".card-body a.btn-outline-success").then(($btn) => {
      const href = $btn.attr("href");
      if (href) {
        cy.wrap($btn).click();
        cy.url().should("include", href);
        cy.visit("/");
      }
    });
  });

  it("Footer", () => {
    cy.get("footer").should("be.visible");
    cy.get("footer").find("a").should("have.length.greaterThan", 0);
  });
});

describe("Base (Staff)", () => {
  beforeEach(() => {
    cy.login('staff', 'staffPass123')
    cy.visit('/')
  })

  it("Main page title", () => {
    cy.get("h1.display-5").should("be.visible").and("not.be.empty");
  });

  it("Navigation bar", () => {
    cy.get("header").should("be.visible");
    cy.get("header nav").should("exist");
    cy.get("header nav").find("a").should("have.length.greaterThan", 0);
  });

  it("User info section", () => {
    cy.get(".card-header").contains("User Info").should("be.visible");

    cy.get("#profile-picture")
      .should("be.visible")
      .and(($img) => {
        expect($img.attr("src")).to.match(/\/static\/images\/default_(superuser|staff|user)\.svg/);
        expect($img.attr("src")).to.include("default_staff.svg");
      });

    cy.get(".card-body a")
      .first()
      .within(() => {
        cy.get("span.badge").should("contain.text", "staff");
      });
  });

  it("Profile link", () => {
    cy.get(".card-body a").first().click();
    cy.url().should("include", "/users/profile");
    cy.visit('/');
  });

  it("User role", () => {
    cy.get(".card-body")
      .first()
      .within(() => {
        cy.get("span.badge").contains("Staff").should("be.visible");
      });
  });

  it("Quick actions", () => {
    cy.contains('.card-header', 'Quick Actions')
      .parent()
      .within(() => {
        cy.get(".card-body a.btn-outline-dark")
          .should("contain.text", "View My Projects")
          .and("have.attr", "href")
          .and("not.be.empty");

        cy.get(".card-body a.btn-outline-primary")
          .should("contain.text", "View My Documents")
          .and("have.attr", "href")
          .and("not.be.empty");

        cy.get("a.btn-outline-success")
          .should("contain.text", "Generate Content")
          .and("have.attr", "href")
          .and("not.be.empty");

        cy.get(".card-body a.btn-outline-danger")
          .should("contain.text", "Test AI Models")
          .and("have.attr", "href")
          .and("not.be.empty");

        cy.get(".card-body a.btn-outline-warning")
          .should("contain.text", "Generate Description")
          .and("have.attr", "href")
          .and("not.be.empty");

        cy.get(".card-body a.btn-outline-info")
          .should("contain.text", "Generate Title")
          .and("have.attr", "href")
          .and("not.be.empty");
      });
  });

  it("Quick action navigation", () => {
    cy.get(".card-body a.btn-outline-success").then(($btn) => {
      const href = $btn.attr("href");
      if (href) {
        cy.wrap($btn).click();
        cy.url().should("include", href);
        cy.visit("/");
      }
    });
  });

  it("Footer", () => {
    cy.get("footer").should("be.visible");
    cy.get("footer").find("a").should("have.length.greaterThan", 0);
  });
});

describe("Base (Superuser)", () => {
  beforeEach(() => {
    cy.login('superuser', 'superuserPass123')
    cy.visit('/')
  })

  it("Main page title", () => {
    cy.get("h1.display-5").should("be.visible").and("not.be.empty");
  });

  it("Navigation bar", () => {
    cy.get("header").should("be.visible");
    cy.get("header nav").should("exist");
    cy.get("header nav").find("a").should("have.length.greaterThan", 0);
  });

  it("User info section", () => {
    cy.get(".card-header").contains("User Info").should("be.visible");

    cy.get("#profile-picture").should("be.visible").and(($img) => {
      expect($img.attr("src")).to.match(/\/static\/images\/default_(superuser|staff|user)\.svg/);
      expect($img.attr("src")).to.include("default_superuser.svg");
    });

    cy.get(".card-body a")
      .first()
      .within(() => {
        cy.get("span.badge").should("contain.text", "superuser");
      });
  });

  it("Profile link", () => {
    cy.get(".card-body a").first().click();
    cy.url().should("include", "/users/profile");
    cy.visit('/');
  });

  it("User role", () => {
    cy.get(".card-body")
      .first()
      .within(() => {
        cy.get("span.badge").contains("Superuser").should("be.visible");
      });
  });

  it("Quick actions", () => {
    cy.contains('.card-header', 'Quick Actions').parent().within(() => {
      cy.get(".card-body a.btn-outline-dark")
        .should("contain.text", "View My Projects")
        .and("have.attr", "href")
        .and("not.be.empty");

      cy.get(".card-body a.btn-outline-primary")
        .should("contain.text", "View My Documents")
        .and("have.attr", "href")
        .and("not.be.empty");

      cy.get("a.btn-outline-success")
        .should("contain.text", "Generate Content")
        .and("have.attr", "href")
        .and("not.be.empty");

      cy.get(".card-body a.btn-outline-danger")
        .should("contain.text", "Test AI Models")
        .and("have.attr", "href")
        .and("not.be.empty");

      cy.get(".card-body a.btn-outline-warning")
        .should("contain.text", "Generate Description")
        .and("have.attr", "href")
        .and("not.be.empty");

      cy.get(".card-body a.btn-outline-info")
        .should("contain.text", "Generate Title")
        .and("have.attr", "href")
        .and("not.be.empty");
    });
  });

  it("Quick action navigation", () => {
    cy.get(".card-body a.btn-outline-success").then(($btn) => {
      const href = $btn.attr("href");
      if (href) {
        cy.wrap($btn).click();
        cy.url().should("include", href);
        cy.visit("/");
      }
    });
  });

  it("Footer", () => {
    cy.get("footer").should("be.visible");
    cy.get("footer").find("a").should("have.length.greaterThan", 0);
  });
});