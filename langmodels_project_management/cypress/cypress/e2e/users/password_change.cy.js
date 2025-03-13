describe("Password Change (User)", () => {
  beforeEach(() => {
    cy.login('user', 'userPass123');
    cy.visit('/users/profile/password');
  });

  it("Title | Header", () => {
    cy.title().should("eq", "Change Password");
    cy.get(".card-title")
      .contains("Change Password")
      .should("be.visible");
  });

  it("Form Fields", () => {
    cy.get('input[name="old_password"]').should("exist");
    cy.get('input[name="new_password1"]').should("exist");
    cy.get('input[name="new_password2"]').should("exist");
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
    cy.get(".card.shadow-lg.border-secondary")
      .contains("Help & Tips")
      .should("be.visible");
    cy.get(".card.shadow-lg.border-secondary")
      .contains("How to Change Your Password")
      .should("be.visible");
  });
});

describe("Password Change (Staff)", () => {
  beforeEach(() => {
    cy.login('staff', 'staffPass123');
    cy.visit('/users/profile/password');
  });

  it("Title | Header", () => {
    cy.title().should("eq", "Change Password");
    cy.get(".card-title")
      .contains("Change Password")
      .should("be.visible");
  });

  it("Form Fields", () => {
    cy.get('input[name="old_password"]').should("exist");
    cy.get('input[name="new_password1"]').should("exist");
    cy.get('input[name="new_password2"]').should("exist");
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
    cy.get(".card.shadow-lg.border-secondary")
      .contains("Help & Tips")
      .should("be.visible");
    cy.get(".card.shadow-lg.border-secondary")
      .contains("How to Change Your Password")
      .should("be.visible");
  });
});

describe("Password Change (Superuser)", () => {
  beforeEach(() => {
    cy.login('superuser', 'superuserPass123');
    cy.visit('/users/profile/password');
  });

  it("Title | Header", () => {
    cy.title().should("eq", "Change Password");
    cy.get(".card-title")
      .contains("Change Password")
      .should("be.visible");
  });

  it("Form Fields", () => {
    cy.get('input[name="old_password"]').should("exist");
    cy.get('input[name="new_password1"]').should("exist");
    cy.get('input[name="new_password2"]').should("exist");
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
    cy.get(".card.shadow-lg.border-secondary")
      .contains("Help & Tips")
      .should("be.visible");
    cy.get(".card.shadow-lg.border-secondary")
      .contains("How to Change Your Password")
      .should("be.visible");
  });
});
