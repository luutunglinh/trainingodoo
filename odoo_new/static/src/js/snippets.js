/** @odoo-module */
import PublicWidget from "@web/legacy/js/public/public_widget";
import {jsonrpc} from "@web/core/network/rpc_service";
import {renderToElement} from "@web/core/utils/render";

var test = PublicWidget.Widget.extend({
    selector: '.book_snippet',
    disabledInEditableMode: false,
    willStart: async function () {
        this.rows = this.el.dataset.numberOfBooks || '5';
    },
    async start() {
        // const data = await jsonrpc('/web/dataset/search_read', {
        //     model: 'book.details',
        //     fields: ['name', 'published_year'],
        //     domain: [],
        //     sort: 'published_year desc',
        // });

        const data = await jsonrpc('/book_details', {});
        console.log(data)
        this.el.innerHTML = ''; // Clear existing content

        data.forEach(book => {
            const row = document.createElement('tr');
            const nameCell = document.createElement('td');
            nameCell.textContent = book.name;
            const dateCell = document.createElement('td');
            dateCell.textContent = book.published_year;
            row.appendChild(nameCell);
            row.appendChild(dateCell);
            this.el.appendChild(row);
        });
    }
},)

PublicWidget.registry.products_category_wise_snippet = test;
return test;
