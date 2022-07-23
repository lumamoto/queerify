// material
import { Container, Typography } from '@mui/material';
// components
import Page from '../components/Page';
import { PlaylistList } from '../sections/@dashboard/playlists';
// mock
import PLAYLISTS from '../data/playlists';

import Searchbar from '../components/Searchbar'

// ----------------------------------------------------------------------

export default function EcommerceShop() {
  return (
    <Page title="Dashboard: Playlists">
      <Container>
        <Typography variant="h4" sx={{ mb: 5 }}>
          Playlists
        </Typography>
        <Searchbar />

        {/* <Stack direction="row" flexWrap="wrap-reverse" alignItems="center" justifyContent="flex-end" sx={{ mb: 5 }}>
            <PlaylistSort />
        </Stack> */}

        <PlaylistList playlists={PLAYLISTS} />
      </Container>
    </Page>
  );
}