describe('Base Authentication', () => {
  beforeEach(() => {
    cy.visit('/authentication/login');
  });

  it('Favicon', () => {
    cy.get('link[rel="icon"]')
      .should('have.attr', 'href')
      .and('include', '/static/images/favicon.ico');
  });

  it('Stylesheet', () => {
    cy.get('link[rel="stylesheet"]')
      .filter('[href*="/static/css/style.css"]')
      .should('exist');
  });

  it('External stylesheets', () => {
    cy.get('link[href*="cdnjs.cloudflare.com"]')
      .should('exist');
  });

  it('Layout', () => {
    cy.get('main.container').should('exist');
    cy.get('body').should('have.class', 'd-flex');
    cy.get('body').should('have.class', 'align-items-center');
    cy.get('body').should('have.class', 'justify-content-center');
  });

  it('Messages', () => {
    cy.get('body').then(($body) => {
      if ($body.find('.messages').length) {
        cy.get('.messages').should('be.visible');
      } else {
        cy.log('No messages rendered on page load.');
      }
    });
  });
});
