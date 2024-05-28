# -*- coding: utf-8 -*-
import werkzeug

from odoo import http
from odoo.http import request
from odoo.tools import json


class OdooNew(http.Controller):
    @http.route('/books', type="http", auth="user", website=True, csrf_token=True)
    def library_books(self, **kw):
        return request.render(
            'odoo_new.books_issue_form', {
                'books': request.env['book.details'].search([]),
            })

    @http.route('/books/<model("book.details"):book>', type="http", auth="user", website=True)
    def library_book_detail(self, book):
        return request.render(
            'odoo_new.book_detail', {
                'book': book,
            }
        )

    @http.route('/book_details', type="json", auth="user")
    def library_book_details(self, **kw):
        books = request.env['book.details'].sudo().search_read([], ['name', 'published_year'],
                                                               order='published_year desc')
        print("books", books)
        return books

    # @http.route('/appointment', auth='public', website=True)
    # def library_books(self, **kw):
    #
    #     return request.render(
    #         'odoo_new.books_issue_formm',{
    #             'books': request.env['book.details'].sudo().search([])
    #         })

    @http.route('/appointment/submit', type='http', auth='public', website=True)
    def library_booksss(self, **kw):
        if kw.get('book_id'):
            book_id = int(kw.get('book_id'))
            issue_description = kw.get('issue_description')
            request.env['book.issue'].sudo().create({
                'book_id': book_id,
                'issue_description': issue_description,
                'submitted_by': request.env.user.id
            })
        return request.render("odoo_new.thankyou",{})

    @http.route('/appointment',type='http', auth='public', website=True)
    def create_library(self, **kw):
        return http.request.render(
            'odoo_new.books_issue_formm', {
                'books': request.env['book.details'].sudo().search([]),
                'submitted': kw.get('submitted', False)
            })


