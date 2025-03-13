describe("Login", () => {
  beforeEach(() => {
    cy.visit("/authentication/login/");
  });

  it("Header", () => {
    cy.get(".card-header").within(() => {
      cy.get("h1").should("contain.text", "Login");
      cy.get("i.fa-arrow-right-to-bracket").should("be.visible");
    });
  });

  it("Placeholders", () => {
    cy.get('form[action="/authentication/login/"]').within(() => {
      cy.get("#username")
        .should("be.visible")
        .and("have.attr", "placeholder", "Enter your username...");
      cy.get("#password")
        .should("be.visible")
        .and("have.attr", "placeholder", "Enter your password...");
    });
  });

  it("Submit button", () => {
    cy.get('form[action="/authentication/login/"]').within(() => {
      cy.get("button[type='submit']")
        .should("be.visible")
        .and("contain.text", "Login");
    });
  });

  it("Register link | Use as Guest", () => {
    cy.get(".card-footer").within(() => {
      cy.contains("Don't have an account?").should("be.visible");
      cy.contains("Register")
        .should("be.visible")
        .and("have.attr", "href")
        .and("include", "register");
      cy.get("form").within(() => {
        cy.get("button")
          .should("be.visible")
          .and("contain.text", "Use as Guest");
      });
    });
  });

  it("Login", () => {
    cy.get('input[name="username"]').type("user")
    cy.get('input[name="password"]').type("userPass123")
    cy.get('form[action="/authentication/login/"]').within(() => {
      cy.get('button[type="submit"]').click();
    });

    cy.url().should("include", "/"); 

    cy.contains("You have successfully logged in!").should("be.visible");
  });
});
