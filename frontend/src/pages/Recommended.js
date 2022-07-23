// material
import { Stack, Container, Typography } from '@mui/material';
// components
import Page from '../components/Page';

// ----------------------------------------------------------------------

export default function Recommended() {
  return (
    <Page title="Recommended Playlist">
      <Container>
        <Stack direction="row" alignItems="center" justifyContent="space-between" mb={5}>
          <Typography variant="h4" gutterBottom>
            Generate a Recommended Playlist
          </Typography>
        </Stack>
      </Container>
    </Page>
  );
}
