describe("Navbar (Guest)", () => {
  beforeEach(() => {
    cy.visit("/");
  });

  it("Projects | Documents", () => {
    cy.get("nav .navbar-nav.me-auto").within(() => {
      cy.contains("Projects").should("not.exist");
      cy.contains("Documents").should("not.exist");
    });
  });

  it("PlayGround dropdown", () => {
    cy.get("nav .navbar-nav.me-auto").within(() => {
      cy.contains("PlayGround").should("be.visible").click();
      cy.get('.dropdown-menu[aria-labelledby="navbarDropdownPlayground"]').within(() => {
        cy.contains("Test Models").should("have.attr", "href").and("not.be.empty");
        cy.contains("Generate Description").should("have.attr", "href").and("not.be.empty");
        cy.contains("Generate Title").should("have.attr", "href").and("not.be.empty");
      });
    });
  });

  it("Login | Register", () => {
    cy.get("nav .navbar-nav.ms-auto").within(() => {
      cy.contains("Login").should("be.visible");
      cy.contains("Register").should("be.visible");
      cy.contains("Profile").should("not.exist");
      cy.contains("Logout").should("not.exist");
      cy.contains("Admin Panel").should("not.exist");
    });
  });
});

describe("Navbar (User)", () => {
  beforeEach(() => {
    cy.login('user', 'userPass123');
    cy.visit('/');
  });

  it("Projects dropdown", () => {
    cy.get("nav .navbar-nav.me-auto").within(() => {
      cy.contains("Projects").should("be.visible").click();
      cy.get('.dropdown-menu[aria-labelledby="navbarDropdownProjects"]').within(() => {
        cy.contains("List Projects").should("have.attr", "href").and("not.be.empty");
        cy.contains("Create Project").should("have.attr", "href").and("not.be.empty");
      });
    });
  });

  it("Documents dropdown", () => {
    cy.get("nav .navbar-nav.me-auto").within(() => {
      cy.contains("Documents").should("be.visible").click();
      cy.get('.dropdown-menu[aria-labelledby="navbarDropdownDocuments"]').within(() => {
        cy.contains("List Documents").should("have.attr", "href").and("not.be.empty");
        cy.contains("Create Document").should("have.attr", "href").and("not.be.empty");
      });
    });
  });

  it("Generate", () => {
    cy.get("nav .navbar-nav.me-auto").within(() => {
      cy.contains("Generate").should("be.visible");
    });
  });

  it("PlayGround dropdown", () => {
    cy.get("nav .navbar-nav.me-auto").within(() => {
      cy.contains("PlayGround").should("be.visible").click();
      cy.get('.dropdown-menu[aria-labelledby="navbarDropdownPlayground"]').within(() => {
        cy.contains("Test Models").should("have.attr", "href").and("not.be.empty");
        cy.contains("Generate Description").should("have.attr", "href").and("not.be.empty");
        cy.contains("Generate Title").should("have.attr", "href").and("not.be.empty");
      });
    });
  });

  it("Profile | Logout", () => {
    cy.get("nav .navbar-nav.ms-auto").within(() => {
      cy.contains("Login").should("not.exist");
      cy.contains("Register").should("not.exist");
      cy.contains("Profile").should("be.visible");
      cy.contains("Logout").should("be.visible");
      cy.contains("Admin Panel").should("not.exist");
    });
  });
});

describe("Navbar (Staff)", () => {
  beforeEach(() => {
    cy.login('staff', 'staffPass123');
    cy.visit('/');
  });

  it("Projects dropdown", () => {
    cy.get("nav .navbar-nav.me-auto").within(() => {
      cy.contains("Projects").should("be.visible").click();
      cy.get('.dropdown-menu[aria-labelledby="navbarDropdownProjects"]').within(() => {
        cy.contains("List Projects").should("have.attr", "href").and("not.be.empty");
        cy.contains("Create Project").should("have.attr", "href").and("not.be.empty");
      });
    });
  });

  it("Documents dropdown", () => {
    cy.get("nav .navbar-nav.me-auto").within(() => {
      cy.contains("Documents").should("be.visible").click();
      cy.get('.dropdown-menu[aria-labelledby="navbarDropdownDocuments"]').within(() => {
        cy.contains("List Documents").should("have.attr", "href").and("not.be.empty");
        cy.contains("Create Document").should("have.attr", "href").and("not.be.empty");
      });
    });
  });

  it("Generate", () => {
    cy.get("nav .navbar-nav.me-auto").within(() => {
      cy.contains("Generate").should("be.visible");
    });
  });

  it("PlayGround dropdown", () => {
    cy.get("nav .navbar-nav.me-auto").within(() => {
      cy.contains("PlayGround").should("be.visible").click();
      cy.get('.dropdown-menu[aria-labelledby="navbarDropdownPlayground"]').within(() => {
        cy.contains("Test Models").should("have.attr", "href").and("not.be.empty");
        cy.contains("Generate Description").should("have.attr", "href").and("not.be.empty");
        cy.contains("Generate Title").should("have.attr", "href").and("not.be.empty");
      });
    });
  });

  it("Profile | Logout", () => {
    cy.get("nav .navbar-nav.ms-auto").within(() => {
      cy.contains("Login").should("not.exist");
      cy.contains("Register").should("not.exist");
      cy.contains("Profile").should("be.visible");
      cy.contains("Logout").should("be.visible");
      cy.contains("Admin Panel").should("not.exist");
    });
  });
});

describe("Navbar (Superuser)", () => {
  beforeEach(() => {
    cy.login('superuser', 'superuserPass123');
    cy.visit('/');
  });

  it("Projects dropdown", () => {
    cy.get("nav .navbar-nav.me-auto").within(() => {
      cy.contains("Projects").should("be.visible").click();
      cy.get('.dropdown-menu[aria-labelledby="navbarDropdownProjects"]').within(() => {
        cy.contains("List Projects").should("have.attr", "href").and("not.be.empty");
        cy.contains("Create Project").should("have.attr", "href").and("not.be.empty");
      });
    });
  });

  it("Documents dropdown", () => {
    cy.get("nav .navbar-nav.me-auto").within(() => {
      cy.contains("Documents").should("be.visible").click();
      cy.get('.dropdown-menu[aria-labelledby="navbarDropdownDocuments"]').within(() => {
        cy.contains("List Documents").should("have.attr", "href").and("not.be.empty");
        cy.contains("Create Document").should("have.attr", "href").and("not.be.empty");
      });
    });
  });

  it("Generate", () => {
    cy.get("nav .navbar-nav.me-auto").within(() => {
      cy.contains("Generate").should("be.visible");
    });
  });

  it("PlayGround dropdown", () => {
    cy.get("nav .navbar-nav.me-auto").within(() => {
      cy.contains("PlayGround").should("be.visible").click();
      cy.get('.dropdown-menu[aria-labelledby="navbarDropdownPlayground"]').within(() => {
        cy.contains("Test Models").should("have.attr", "href").and("not.be.empty");
        cy.contains("Generate Description").should("have.attr", "href").and("not.be.empty");
        cy.contains("Generate Title").should("have.attr", "href").and("not.be.empty");
      });
    });
  });

  it("Admin Panel | Profile | Logout", () => {
    cy.get("nav .navbar-nav.ms-auto").within(() => {
      cy.contains("Login").should("not.exist");
      cy.contains("Register").should("not.exist");
      cy.contains("Admin Panel").should("be.visible");
      cy.contains("Profile").should("be.visible");
      cy.contains("Logout").should("be.visible");
    });
  });
});