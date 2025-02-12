module.exports = configure(function (ctx) {
  return {
    css: ['app.scss'],
    extras: [
      'material-icons'
    ],
    framework: {
      plugins: ['Notify', 'Loading']
    }
  }
})