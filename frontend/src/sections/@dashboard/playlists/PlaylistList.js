import PropTypes from 'prop-types';
// material
import { Grid } from '@mui/material';
import PlaylistCard from './PlaylistCard';

// ----------------------------------------------------------------------

PlaylistList.propTypes = {
  playlists: PropTypes.array.isRequired
};

export default function PlaylistList({ playlists, ...other }) {
  return (
    <Grid container spacing={3} {...other}>
      {playlists.map((playlist) => (
        <Grid key={playlist.id} item xs={12} sm={6} md={3}>
          <PlaylistCard playlist={playlist} />
        </Grid>
      ))}
    </Grid>
  );
}
