describe('Messages', () => {
    beforeEach(() => {
        cy.visit('/');
    });

    it('Success message', () => {
        cy.get('body').then(($body) => {
            if ($body.find('.alert-success').length) {
                cy.get('.alert-success')
                    .should('be.visible')
                    .and('contain', 'success');
                cy.get('.alert-success i.fas.fa-check-circle.text-success').should('exist');
            }
        });
    });

    it('Error message', () => {
        cy.get('body').then(($body) => {
            if ($body.find('.alert-danger').length) {
                cy.get('.alert-danger')
                    .should('be.visible')
                    .and('contain', 'error');
                cy.get('.alert-danger i.fas.fa-times-circle.text-danger').should('exist');
            }
        });
    });

    it('Warning message', () => {
        cy.get('body').then(($body) => {
            if ($body.find('.alert-warning').length) {
                cy.get('.alert-warning')
                    .should('be.visible')
                    .and('contain', 'warning');
                cy.get('.alert-warning i.fas.fa-exclamation-triangle.text-warning').should('exist');
            }
        });
    });

    it('Info message', () => {
        cy.get('body').then(($body) => {
            if ($body.find('.alert-info').length) {
                cy.get('.alert-info')
                    .should('be.visible')
                    .and('contain', 'info');
                cy.get('.alert-info i.fas.fa-info-circle.text-info').should('exist');
            }
        });
    });
});
