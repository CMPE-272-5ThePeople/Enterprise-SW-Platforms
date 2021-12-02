function requireHTTPS(req, res, next) {
    // The 'x-forwarded-proto' check is for Heroku
    if (!req.secure && req.get('x-forwarded-proto') !== 'https') {
        return res.redirect('https://' + req.get('host') + req.url);
    }
    next();
}
const express = require('express');
const app = express();
app.use(requireHTTPS);
app.get('/*', (request, response) => {
	response.sendFile(path.join(__dirname, 'client/build', 'index.html'));
});
app.use(express.static('./dist/web-enterprise-sw-platforms'));
if (process.env.NODE_ENV === 'production') {
	app.use(express.static('client/build'));
}
app.listen(process.env.PORT || 8080);