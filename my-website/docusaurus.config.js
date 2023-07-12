const lightCodeTheme = require('prism-react-renderer/themes/github');
const darkCodeTheme = require('prism-react-renderer/themes/dracula');

// With JSDoc @type annotations, IDEs can provide config autocompletion
/** @type {import('@docusaurus/types').DocusaurusConfig} */
(module.exports = {
  title: "Mobid - Codes",
  tagline: 'Welcome to My Codes Documentary, Explore It :)',
  url: 'https://MdMobid.github.io',
  baseUrl: '/codes/',
  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',
  favicon: 'img/favicon.ico',
  organizationName: 'MdMobid', // Usually your GitHub org/user name.
  projectName: 'codes', // Usually your repo name.

  presets: [
    [
      '@docusaurus/preset-classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: require.resolve('./sidebars.js'),
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      navbar: {
        title: 'Mobid',
        logo: {
          alt: 'Mobid',
          src: 'img/logo.svg',
        },
        items: [
          {
            type: 'doc',
            docId: 'Class-11/intro',
            position: 'left',
            label: 'Class 11',
          },
          {
            type: 'doc',
            docId: 'Class-12/intro',
            position: 'left',
            label: 'Class 12',
          },
          {
            href: 'https://github.com/MdMobid',
            label: 'GitHub',
            position: 'right',
          },
        ],
      },
      trailingSlash: true, // Add this line to enable trailing slashes
      footer: {
        style: 'dark',
        links: [
          {
            title: 'Docs',
            items: [
              {
                label: 'Class 11',
                to: '/docs/Class-11/intro',
              },
              {
                label: 'Class 12',
                to: '/docs/Class-12/intro',
              },
            ],
          },
          {
            title: 'More',
            items: [
              /*{
                label: 'Blog',
                to: '/blog',
              },*/
              {
                label: 'GitHub',
                href: 'https://github.com/MdMobid',
              },
              {
                label: 'Telegram',
                href: 'https://telegram.me/MobidX',
              },
            ],
          },
        ],
        copyright: `Copyright © ${new Date().getFullYear()} <a href="https://github.com/MdMobid" target="_blank">Md Mobid Hossain</a>`,
      },
      prism: {
        theme: lightCodeTheme,
        darkTheme: darkCodeTheme,
      },
    }),
});
