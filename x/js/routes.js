routes = [
  {
    path: '/',
    url: '/index/',
  },
  {
    path: '/:id/',
    url: '/section/{{id}}',
  },
  {
    path: '/new',
    url: './pages/new.php',
  },
    {
    path: '/pubgsafe',
    url: './pages/pubgsafe.php',
  },
  
  {
    path: '/appleid',
    url: './pages/appleid.php',
  },
  {
    path: '/odyssey',
    url: './pages/odyssey.php',
  },
  {
    path: '/esign',
    url: './pages/esign.php',
  },
  {
     path: '/scarlet',
       url: './pages/scarlet.php',
  },
  {
    path: '/ppsspp',
    url: './pages/ppsspp.php',
  },
  {
    path: '/bolt',
    url: './pages/bolt.php',
  },
  {
    path: '/procam',
    url: './pages/procam.php',
  },
  {
    path: '/tiktok',
    url: './pages/tiktok.php',
  },
  {
    path: '/unc0ver',
    url: './pages/unc0ver.php',
  },
  {
    path: '/pubgv2',
    url: './pages/pubgv2.php',
  },
  {
    path: '/pubgv3',
    url: './pages/pubgv3.php',
  },

  {
    path: '/alone',
    url: './aloneios.mobileconfig',
  },
  {
    path: '/videostar',
    url: './pages/videostar.php',
  },
  {
    path: '/pubg',
    url: './pages/pubg.php',
  },
  {
    path: '/gta',
    url: './pages/gta.php',
  },
  {
    path: '/org',
    url: './pages/org.php',
  },
  {
    path: '/8ball',
    url: './pages/8ball.php',
  },
  {
    path: '/appcake',
    url: './pages/appcake.php',
  },
  {
    path: '/minecraft',
    url: './pages/minecraft.php',
  },
  {
    path: '/videofx',
    url: './pages/videofx.php',
  },
  {
    path: '/picsart',
    url: './pages/picsart.php',
  },
  {
    path: '/Kinemaster',
    url: './pages/kinemaster.php',
  },
  {
    path: '/pages/:id',
    url: './pages/{{id}}',
  },
  {
    path: '/vdhack',
    url: './pages/vdhack.php',
  },
  {
    path: '/djay',
    url: './pages/djay.php',
  },
    {
      path: '/snap',
      url: './pages/snapchat.php',
    },
  {
    path: '/theming',
    componentUrl: './pages/theme.php',
  },
  // Default route (404 page). MUST BE THE LAST
  {
    path: '(.*)',
    url: './pages/404.php',
  },
];
