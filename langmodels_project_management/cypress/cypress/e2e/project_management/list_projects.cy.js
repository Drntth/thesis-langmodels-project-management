describe("List Projects (User)", () => {
  beforeEach(() => {
    cy.login('user', 'userPass123')
    cy.visit('/projects/list');
  });

  it("Title", () => {
    cy.title().should('eq', 'List Projects');
  });

  it("Create New Project", () => {
    cy.get('a.btn.btn-success')
      .contains('Create New Project')
      .should('be.visible')
      .and('have.attr', 'href')
      .and('include', '/projects/create');
  });

  it("Cards", () => {
    cy.get('body').then($body => {
      if ($body.find('.card.h-100.shadow-lg.border-dark').length) {
        cy.get('.card.h-100.shadow-lg.border-dark').its('length').should('be.gte', 1);
      } else {
        cy.contains('No projects available.').should('be.visible');
      }
    });
  });

  it("View", () => {
    cy.get('body').then($body => {
      if ($body.find('.card.h-100.shadow-lg.border-dark').length) {
        cy.get('.card.h-100.shadow-lg.border-dark').each($card => {
          cy.wrap($card)
            .find('a.btn.btn-md.btn-secondary')
            .contains('View')
            .should('be.visible')
            .and('have.attr', 'href')
            .and('include', '/projects');
        });
      }
    });
  });

  it("Memberships", () => {
    cy.get('body').then($body => {
      if ($body.find('.card.shadow-lg.border-secondary').length) {
        cy.get('.card.shadow-lg.border-secondary')
          .contains('Project Memberships')
          .should('be.visible');
      }
    });
  });

  it("Help & Tips", () => {
    cy.get('.card.shadow-lg.border-secondary')
      .contains('Help & Tips')
      .should('be.visible');
    cy.get('.card.shadow-lg.border-secondary')
      .contains('How to Create a Project')
      .should('be.visible');
    cy.get('.card.shadow-lg.border-secondary')
      .contains('How to View Project Details')
      .should('be.visible');
    cy.get('.card.shadow-lg.border-secondary')
      .contains('Project Status Explanation')
      .should('be.visible');
  });
});

describe("List Projects (Staff)", () => {
  beforeEach(() => {
    cy.login('staff', 'staffPass123')
    cy.visit('/projects/list');
  });

  it("Title", () => {
    cy.title().should('eq', 'List Projects');
  });

  it("Create New Project", () => {
    cy.get('a.btn.btn-success')
      .contains('Create New Project')
      .should('be.visible')
      .and('have.attr', 'href')
      .and('include', '/projects/create');
  });

  it("Cards", () => {
    cy.get('body').then($body => {
      if ($body.find('.card.h-100.shadow-lg.border-dark').length) {
        cy.get('.card.h-100.shadow-lg.border-dark').its('length').should('be.gte', 1);
      } else {
        cy.contains('No projects available.').should('be.visible');
      }
    });
  });

  it("View", () => {
    cy.get('body').then($body => {
      if ($body.find('.card.h-100.shadow-lg.border-dark').length) {
        cy.get('.card.h-100.shadow-lg.border-dark').each($card => {
          cy.wrap($card)
            .find('a.btn.btn-md.btn-secondary')
            .contains('View')
            .should('be.visible')
            .and('have.attr', 'href')
            .and('include', '/projects');
        });
      }
    });
  });

  it("Memberships", () => {
    cy.get('body').then($body => {
      if ($body.find('.card.shadow-lg.border-secondary').length) {
        cy.get('.card.shadow-lg.border-secondary')
          .contains('Project Memberships')
          .should('be.visible');
      }
    });
  });

  it("Help & Tips", () => {
    cy.get('.card.shadow-lg.border-secondary')
      .contains('Help & Tips')
      .should('be.visible');
    cy.get('.card.shadow-lg.border-secondary')
      .contains('How to Create a Project')
      .should('be.visible');
    cy.get('.card.shadow-lg.border-secondary')
      .contains('How to View Project Details')
      .should('be.visible');
    cy.get('.card.shadow-lg.border-secondary')
      .contains('Project Status Explanation')
      .should('be.visible');
  });
});

describe("List Projects (Superuser)", () => {
  beforeEach(() => {
    cy.login('superuser', 'superuserPass123');
    cy.visit('/projects/list');
  });

  it("Title", () => {
    cy.title().should('eq', 'List Projects');
  });

  it("Create New Project", () => {
    cy.get('a.btn.btn-success')
      .contains('Create New Project')
      .should('be.visible')
      .and('have.attr', 'href')
      .and('include', '/projects/create');
  });

  it("Cards", () => {
    cy.get('body').then($body => {
      if ($body.find('.card.h-100.shadow-lg.border-dark').length) {
        cy.get('.card.h-100.shadow-lg.border-dark').its('length').should('be.gte', 1);
      } else {
        cy.contains('No projects available.').should('be.visible');
      }
    });
  });

  it("View", () => {
    cy.get('body').then($body => {
      if ($body.find('.card.h-100.shadow-lg.border-dark').length) {
        cy.get('.card.h-100.shadow-lg.border-dark').each($card => {
          cy.wrap($card)
            .find('a.btn.btn-md.btn-secondary')
            .contains('View')
            .should('be.visible')
            .and('have.attr', 'href')
            .and('include', '/projects');
        });
      }
    });
  });

  it("Memberships", () => {
    cy.get('body').then($body => {
      if ($body.find('.card.shadow-lg.border-secondary').length) {
        cy.get('.card.shadow-lg.border-secondary')
          .contains('Project Memberships')
          .should('be.visible');
      }
    });
  });

  it("Help & Tips", () => {
    cy.get('.card.shadow-lg.border-secondary')
      .contains('Help & Tips')
      .should('be.visible');
    cy.get('.card.shadow-lg.border-secondary')
      .contains('How to Create a Project')
      .should('be.visible');
    cy.get('.card.shadow-lg.border-secondary')
      .contains('How to View Project Details')
      .should('be.visible');
    cy.get('.card.shadow-lg.border-secondary')
      .contains('Project Status Explanation')
      .should('be.visible');
  });
});
