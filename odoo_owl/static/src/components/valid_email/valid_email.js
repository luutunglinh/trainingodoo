/** @odoo-module **/

import {registry} from '@web/core/registry';
import {EmailField, emailField} from "@web/views/fields/email/email_field";

export class ValidEmailField extends EmailField {
    setup(){
        super.setup()
        console.log("Email")
        console.log(this.props)
    }
}
ValidEmailField.template= "odoo_owl.ValidEmailField"

export const fieldValidEmail = {
    ...emailField,
    component: ValidEmailField,
};

registry.category("fields").add("valid_email",fieldValidEmail)