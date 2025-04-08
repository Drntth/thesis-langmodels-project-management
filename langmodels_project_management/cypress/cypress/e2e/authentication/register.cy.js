describe('Register', () => {
  beforeEach(() => {
    cy.visit('/authentication/register'); 
  });

  it("Header", () => {
    cy.get(".card-header").within(() => {
      cy.get("h1").should("contain.text", "Register");
      cy.get("i.fa-user-plus").should("be.visible");
    });
  });

  it("Placeholders", () => {
    cy.get('form[action="/authentication/register/"]').within(() => {
      cy.get("#username")
        .should("be.visible")
        .and("have.attr", "placeholder", "Enter your username...");
      cy.get("#email")
        .should("be.visible")
        .and("have.attr", "placeholder", "Enter your email address...");
      cy.get("#first_name")
        .should("be.visible")
        .and("have.attr", "placeholder", "Enter your first name here...");
      cy.get("#last_name")
        .should("be.visible")
        .and("have.attr", "placeholder", "Enter your last name here...");
      cy.get("#password")
        .should("be.visible")
        .and("have.attr", "placeholder", "Enter your password...");
      cy.get("#confirm_password")
        .should("be.visible")
        .and("have.attr", "placeholder", "Confirm your password...");
    });
  });

  it("Submit button", () => {
    cy.get('form[action="/authentication/register/"]').within(() => {
      cy.get("button[type='submit']")
        .should("be.visible")
        .and("contain.text", "Register");
    });
  });

  it("Login link | Use as Guest", () => {
    cy.get(".card-footer").within(() => {
      cy.contains("Already have an account?").should("be.visible");
      cy.contains("Login")
        .should("be.visible")
        .and("have.attr", "href")
        .and("include", "login");
      cy.get("form").within(() => {
        cy.get("button")
          .should("be.visible")
          .and("contain.text", "Use as Guest");
      });
    });
  });

  it("Register", () => {
    cy.get('input[name="username"]').type("testuser")
    cy.get('input[name="email"]').type("testuser@example.com")
    cy.get('input[name="first_name"]').type("Elek")
    cy.get('input[name="last_name"]').type("Teszt")
    cy.get('input[name="password1"]').type("testuserPass123")
    cy.get('input[name="password2"]').type("testuserPass123")

    cy.get('form[action="/authentication/register/"]').within(() => {
      cy.get('button[type="submit"]').click();
    });

    cy.url().should("include", "/"); 
  });

  it("Register Error", () => {
    cy.get('input[name="username"]').type("testuser")
    cy.get('input[name="email"]').type("testuser@example.com")
    cy.get('input[name="first_name"]').type("Elek")
    cy.get('input[name="last_name"]').type("Teszt")
    cy.get('input[name="password1"]').type("testuserPass123")
    cy.get('input[name="password2"]').type("testuserPass123")

    cy.get('form[action="/authentication/register/"]').within(() => {
      cy.get('button[type="submit"]').click();
    });

    cy.url().should("include", "/authentication/register/"); 

    cy.contains("A user with that username already exists.").should("be.visible");
  });

  it('Delete test user', () => {
    cy.visit("/authentication/login");
    cy.get('input[name="username"]').type("testuser")
    cy.get('input[name="password"]').type("testuserPass123")
    cy.get('form[action="/authentication/login/"]').within(() => {
      cy.get('button[type="submit"]').click();
    });

    cy.url().should("include", "/"); 

    cy.visit("/users/profile");

    cy.get('form[action*="profile/delete"]').should('exist');
    cy.get('form[onsubmit*="Are you sure you want to delete your profile and all related data? This action cannot be undone."]').should('exist');

    cy.get('form[action*="/users/profile/delete"]').within(() => {
      cy.get('button[type="submit"]').click();
    });
    cy.on('window:confirm', (message) => {
      expect(message).to.include('Are you sure you want to delete your profile and all related data? This action cannot be undone.');
      return true;
    });
  });
});
