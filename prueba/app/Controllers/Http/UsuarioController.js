'use strict'
const User = use('App/Models/User');
class UsuarioController {

    async registro({ request, response }) {
        const { name, email, password } = request.only(['name', 'email', 'password'])

        await User.create({
            name,
            email,
            password
        })
        return response.send({ message: 'Has sido registrado adonis' })
    }
}

module.exports = UsuarioController