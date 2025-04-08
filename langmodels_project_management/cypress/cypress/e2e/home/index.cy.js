describe('Index (Guest)', () => {
  beforeEach(() => {
    cy.visit('/');
  });

  it('Title | Header', () => {
    cy.title().should('eq', 'Home');
    cy.contains('Welcome to the Language Models in Project Management Application!').should('be.visible');
  });

  it('AI-Powered Project Management section', () => {
    cy.contains('AI-Powered Project Management').should('be.visible');
    cy.contains('Experience a smarter way to manage projects').should('be.visible');
  });

  it('Get Started', () => {
    cy.get('a.btn.btn-primary.btn-lg')
      .should('be.visible')
      .and('have.attr', 'href')
      .then((href) => {
        expect(href).to.contain('/projects');
      });
    cy.get('a.btn.btn-primary.btn-lg')
      .should('be.visible')
      .click();
    cy.url().should('include', '/login');
  });

  it('Current Projects', () => {
    cy.contains('Current Projects').should('be.visible');
    cy.get('.card-header.bg-dark.text-white').its('length').should('be.gte', 0);
  });

  it('Key Features', () => {
    cy.contains('h3', 'Key Features')
    .closest('div.col-12')
    .within(() => {
      cy.contains('Projects').should('be.visible');
      cy.contains('Documents').should('be.visible');
      cy.contains('Generate').should('be.visible');
      cy.contains('PlayGround').should('be.visible');
    });
  });

  it('By the Numbers', () => {
    cy.contains('By the Numbers').should('be.visible');
    cy.contains('Projects Created').should('be.visible');
    cy.contains('Documents Generated').should('be.visible');
    cy.contains('Active Users').should('be.visible');
  });

  it('Sign Up Now', () => {
    cy.get('a.btn.btn-light.btn-lg')
      .contains('Sign Up Now')
      .should('be.visible')
      .and('have.attr', 'href')
      .then((href) => {
        expect(href).to.contain('/authentication/register');
      });
      cy.get('a.btn.btn-light.btn-lg')
      .should('be.visible')
      .click();
    cy.url().should('include', '/authentication/register');
  });
});

describe("Index (User)", () => {
  beforeEach(() => {
    cy.login('user', 'userPass123')
    cy.visit('/')
  })

  it('Title | Header', () => {
    cy.title().should('eq', 'Home');
    cy.contains('Welcome to the Language Models in Project Management Application!').should('be.visible');
  });

  it('AI-Powered Project Management section', () => {
    cy.contains('AI-Powered Project Management').should('be.visible');
    cy.contains('Experience a smarter way to manage projects').should('be.visible');
  });

  it('Get Started', () => {
    cy.get('a.btn.btn-primary.btn-lg')
      .should('be.visible')
      .and('have.attr', 'href')
      .then((href) => {
        expect(href).to.contain('/projects');
      });
    cy.get('a.btn.btn-primary.btn-lg')
      .should('be.visible')
      .click();
    cy.url().should('include', '/projects/list');
  });

  it('Current Projects', () => {
    cy.contains('Current Projects').should('be.visible');
    cy.get('.card-header.bg-dark.text-white').its('length').should('be.gte', 0);
  });

  it('Key Features', () => {
    cy.contains('h3', 'Key Features')
    .closest('div.col-12')
    .within(() => {
      cy.contains('Projects').should('be.visible');
      cy.contains('Documents').should('be.visible');
      cy.contains('Generate').should('be.visible');
      cy.contains('PlayGround').should('be.visible');
    });
  });

  it('By the Numbers', () => {
    cy.contains('By the Numbers').should('be.visible');
    cy.contains('Projects Created').should('be.visible');
    cy.contains('Documents Generated').should('be.visible');
    cy.contains('Active Users').should('be.visible');
  });
});
