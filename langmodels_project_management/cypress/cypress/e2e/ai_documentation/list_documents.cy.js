describe("List Documents (User)", () => {
  beforeEach(() => {
    cy.login('user', 'userPass123')
    cy.visit('/ai-docs/list');
  });

  it("Title", () => {
    cy.title().should('eq', 'List Documents');
  });

  it("Create New Document", () => {
    cy.get('a.btn.btn-success')
      .contains('Create New Document')
      .should('be.visible')
      .and('have.attr', 'href')
      .and('include', '/ai-docs/create');
  });

  it("Cards", () => {
    cy.get('body').then($body => {
      if ($body.find('.card.h-100.shadow-lg.border-dark').length) {
        cy.get('.card.h-100.shadow-lg.border-dark').its('length').should('be.gte', 1);
      } else {
        cy.contains('No documents available.').should('be.visible');
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
            .and('include', '/ai-docs');
        });
      }
    });
  });

  it("Help & Tips", () => {
    cy.get('.card.shadow-lg.border-secondary')
      .contains('Help & Tips')
      .should('be.visible');
    cy.get('.card.shadow-lg.border-secondary')
      .contains('Create a New Document')
      .should('be.visible');
    cy.get('.card.shadow-lg.border-secondary')
      .contains('View Document Details')
      .should('be.visible');
    cy.get('.card.shadow-lg.border-secondary')
      .contains('Project Association')
      .should('be.visible');
  });
});

describe("List Documents (Staff)", () => {
  beforeEach(() => {
    cy.login('staff', 'staffPass123')
    cy.visit('/ai-docs/list');
  });

  it("Title", () => {
    cy.title().should('eq', 'List Documents');
  });

  it("Create New Document", () => {
    cy.get('a.btn.btn-success')
      .contains('Create New Document')
      .should('be.visible')
      .and('have.attr', 'href')
      .and('include', '/ai-docs/create');
  });

  it("Cards", () => {
    cy.get('body').then($body => {
      if ($body.find('.card.h-100.shadow-lg.border-dark').length) {
        cy.get('.card.h-100.shadow-lg.border-dark').its('length').should('be.gte', 1);
      } else {
        cy.contains('No documents available.').should('be.visible');
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
            .and('include', '/ai-docs');
        });
      }
    });
  });

  it("Help & Tips", () => {
    cy.get('.card.shadow-lg.border-secondary')
      .contains('Help & Tips')
      .should('be.visible');
    cy.get('.card.shadow-lg.border-secondary')
      .contains('Create a New Document')
      .should('be.visible');
    cy.get('.card.shadow-lg.border-secondary')
      .contains('View Document Details')
      .should('be.visible');
    cy.get('.card.shadow-lg.border-secondary')
      .contains('Project Association')
      .should('be.visible');
  });
});

describe("List Documents (Superuser)", () => {
  beforeEach(() => {
    cy.login('superuser', 'superuserPass123');
    cy.visit('/ai-docs/list');
  });

  it("Title", () => {
    cy.title().should('eq', 'List Documents');
  });

  it("Create New Document", () => {
    cy.get('a.btn.btn-success')
      .contains('Create New Document')
      .should('be.visible')
      .and('have.attr', 'href')
      .and('include', '/ai-docs/create');
  });

  it("Cards", () => {
    cy.get('body').then($body => {
      if ($body.find('.card.h-100.shadow-lg.border-dark').length) {
        cy.get('.card.h-100.shadow-lg.border-dark').its('length').should('be.gte', 1);
      } else {
        cy.contains('No documents available.').should('be.visible');
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
            .and('include', '/ai-docs');
        });
      }
    });
  });

  it("Help & Tips", () => {
    cy.get('.card.shadow-lg.border-secondary')
      .contains('Help & Tips')
      .should('be.visible');
    cy.get('.card.shadow-lg.border-secondary')
      .contains('Create a New Document')
      .should('be.visible');
    cy.get('.card.shadow-lg.border-secondary')
      .contains('View Document Details')
      .should('be.visible');
    cy.get('.card.shadow-lg.border-secondary')
      .contains('Project Association')
      .should('be.visible');
  });
});
