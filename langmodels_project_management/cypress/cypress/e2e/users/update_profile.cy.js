describe("Update Profile (User)", () => {
  beforeEach(() => {
    cy.login('user', 'userPass123');
    cy.visit('/users/profile/update');
  });

  it("Title | Header", () => {
    cy.title().should("eq", "Update Profile");
    cy.get(".card-title")
      .contains("Update Profile")
      .should("be.visible");
  });

  it("Form Fields", () => {
    cy.get('input[name="username"]').should("have.value", "user");
    cy.get('input[name="email"]').should("have.value", "user@example.com");
    cy.get('input[name="first_name"]');
    cy.get('input[name="last_name"]');
  });

  it("Security Settings", () => {
    cy.contains(".card", "Security Settings").should("be.visible");
    cy.get("a")
      .contains("Change Password")
      .should("have.attr", "href")
      .and("include", "/users/profile/password/");
  });

  it("Cancel | Update Buttons", () => {
    cy.get("a.btn.btn-secondary")
      .contains("Cancel")
      .should("be.visible")
      .and("have.attr", "href")
      .and("include", "/users/profile/");

    cy.get("button[type='submit']")
      .contains("Update")
      .should("be.visible");
  });

  it("Sidebar Help & Tips", () => {
    cy.get(".card")
      .contains("Help & Tips")
      .should("be.visible");
  });
});

describe("Update Profile (Staff)", () => {
  beforeEach(() => {
    cy.login('staff', 'staffPass123')
    cy.visit('/users/profile/update');
  });

  it("Title | Header", () => {
    cy.title().should("eq", "Update Profile");
    cy.get(".card-title")
      .contains("Update Profile")
      .should("be.visible");
  });

  it("Form Fields", () => {
    cy.get('input[name="username"]').should("have.value", "staff");
    cy.get('input[name="email"]').should("have.value", "staff@example.com");
    cy.get('input[name="first_name"]');
    cy.get('input[name="last_name"]');
  });

  it("Security Settings", () => {
    cy.contains(".card", "Security Settings").should("be.visible");
    cy.get("a")
      .contains("Change Password")
      .should("have.attr", "href")
      .and("include", "/users/profile/password/");
  });

  it("Cancel | Update Buttons", () => {
    cy.get("a.btn.btn-secondary")
      .contains("Cancel")
      .should("be.visible")
      .and("have.attr", "href")
      .and("include", "/users/profile/");

    cy.get("button[type='submit']")
      .contains("Update")
      .should("be.visible");
  });

  it("Sidebar Help & Tips", () => {
    cy.get(".card")
      .contains("Help & Tips")
      .should("be.visible");
  });
});

describe("Update Profile (Superuser)", () => {
  beforeEach(() => {
    cy.login('superuser', 'superuserPass123')
    cy.visit('/users/profile/update');
  });

  it("Title | Header", () => {
    cy.title().should("eq", "Update Profile");
    cy.get(".card-title")
      .contains("Update Profile")
      .should("be.visible");
  });

  it("Form Fields", () => {
    cy.get('input[name="username"]').should("have.value", "superuser");
    cy.get('input[name="email"]').should("have.value", "superuser@example.com");
    cy.get('input[name="first_name"]');
    cy.get('input[name="last_name"]');
  });

  it("Security Settings", () => {
    cy.contains(".card", "Security Settings").should("be.visible");
    cy.get("a")
      .contains("Change Password")
      .should("have.attr", "href")
      .and("include", "/users/profile/password/");
  });

  it("Cancel | Update Buttons", () => {
    cy.get("a.btn.btn-secondary")
      .contains("Cancel")
      .should("be.visible")
      .and("have.attr", "href")
      .and("include", "/users/profile/");

    cy.get("button[type='submit']")
      .contains("Update")
      .should("be.visible");
  });

  it("Sidebar Help & Tips", () => {
    cy.get(".card")
      .contains("Help & Tips")
      .should("be.visible");
  });
});