describe("Profile Page (User)", () => {
  beforeEach(() => {
    cy.login("user", "userPass123");
    cy.visit("/users/profile");
  });

  it("Title | Header", () => {
    cy.title().should("eq", "Profile");
    cy.get(".card-title")
      .contains("Profile")
      .should("be.visible");
  });

  it("Profile picture", () => {
    cy.get('img[alt="Profile Picture"]').should("be.visible");
  });

  it("Informations", () => {
    cy.contains("Username").should("be.visible");
    cy.contains("Email").should("be.visible");
    cy.contains("First Name").should("be.visible");
    cy.contains("Last Name").should("be.visible");
  });

  it("Account status", () => {
    cy.contains("Account Status").should("be.visible");
    cy.contains("Staff Status").should("be.visible");
    cy.contains("Superuser Status").should("be.visible");
  });

  it("Update | Delete", () => {
    cy.get("a.btn.btn-warning")
      .contains("Update")
      .should("be.visible");

    cy.get("button.btn.btn-danger")
      .contains("Delete")
      .should("be.visible");
  });

  it("Help & Tips", () => {
    cy.get(".card")
      .contains("Help & Tips")
      .should("be.visible");
  });
});

describe("Profile Page (Staff)", () => {
  beforeEach(() => {
    cy.login("staff", "staffPass123");
    cy.visit("/users/profile");
  });

  it("Title | Header", () => {
    cy.title().should("eq", "Profile");
    cy.get(".card-title")
      .contains("Profile")
      .should("be.visible");
  });

  it("Profile picture", () => {
    cy.get('img[alt="Profile Picture"]').should("be.visible");
  });

  it("Informations", () => {
    cy.contains("Username").should("be.visible");
    cy.contains("Email").should("be.visible");
    cy.contains("First Name").should("be.visible");
    cy.contains("Last Name").should("be.visible");
  });

  it("Account status", () => {
    cy.contains("Account Status").should("be.visible");
    cy.contains("Staff Status").should("be.visible");
    cy.contains("Superuser Status").should("be.visible");
  });

  it("Update | Delete", () => {
    cy.get("a.btn.btn-warning")
      .contains("Update")
      .should("be.visible");
    cy.get("button.btn.btn-danger")
      .contains("Delete")
      .should("be.visible");
  });

  it("Help & Tips", () => {
    cy.get(".card")
      .contains("Help & Tips")
      .should("be.visible");
  });
});

describe("Profile Page (Superuser)", () => {
  beforeEach(() => {
    cy.login("superuser", "superuserPass123");
    cy.visit("/users/profile");
  });

  it("Title | Header", () => {
    cy.title().should("eq", "Profile");
    cy.get(".card-title")
      .contains("Profile")
      .should("be.visible");
  });

  it("Profile picture", () => {
    cy.get('img[alt="Profile Picture"]').should("be.visible");
  });

  it("Informations", () => {
    cy.contains("Username").should("be.visible");
    cy.contains("Email").should("be.visible");
    cy.contains("First Name").should("be.visible");
    cy.contains("Last Name").should("be.visible");
  });

  it("Account status", () => {
    cy.contains("Account Status").should("be.visible");
    cy.contains("Staff Status").should("be.visible");
    cy.contains("Superuser Status").should("be.visible");
  });

  it("Update | Delete", () => {
    cy.get("a.btn.btn-warning")
      .contains("Update")
      .should("be.visible");
    cy.get("button.btn.btn-danger")
      .contains("Delete")
      .should("be.visible");
  });

  it("Help & Tips", () => {
    cy.get(".card")
      .contains("Help & Tips")
      .should("be.visible");
  });
});
