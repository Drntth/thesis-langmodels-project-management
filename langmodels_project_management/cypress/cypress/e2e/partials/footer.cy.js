describe('Footer', () => {
    beforeEach(() => {
        cy.visit('/');
    });

    it('Visible', () => {
        cy.get('footer.footer').should('be.visible');
    });

    it('Copyright year', () => {
        const currentYear = new Date().getFullYear();
        cy.get('footer.footer p').should('contain.text', `© ${currentYear} Language Models in Project Management`);
    });

    it('Robot icon link', () => {
        cy.get('footer.footer a').should('have.attr', 'href', '/');
        cy.get('footer.footer a i.fa-robot').should('be.visible');
    });
});