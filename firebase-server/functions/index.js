const functions = require('firebase-functions');
const cors = require('cors')({ origin: true })
const admin = require('firebase-admin')

admin.initializeApp()

const database = admin.database().ref('/Attendance')

const getItemsFromDatabase = (res) => {
    let items = [];

    return database.on('value', (snapshot) => {
        snapshot.forEach((item) => {
            items.push({
                id: item.key,
                item: item.val().item
            });
        });
        res.status(200).json(items);
    }, (error) => {
        res.status(error.code).json({
            message: `Something went wrong. ${error.message}`
        })
    })
}

exports.getItems = functions.https.onRequest((req, res) => {
    return cors(req, res, () => {
        if (req.method !== 'GET') {
            return res.status(401).json({
                message: 'Not allowed'
            })
        }
        getItemsFromDatabase(res)
    })
})