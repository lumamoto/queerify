// component
import Iconify from '../../components/Iconify';

// ----------------------------------------------------------------------

const getIcon = (name) => <Iconify icon={name} width={22} height={22} />;

const navConfig = [
  {
    title: 'dashboard',
    path: '/dashboard/app',
    icon: getIcon('eva:pie-chart-2-fill'),
  },
  {
    title: 'recommended',
    path: '/dashboard/recommended',
    icon: getIcon('eva:people-fill'),
  },
  {
    title: 'playlists',
    path: '/dashboard/playlists',
    icon: getIcon('eva:shopping-bag-fill'),
  }
];

export default navConfig;
