import { faker } from '@faker-js/faker';

// ----------------------------------------------------------------------

const PLAYLIST_DICT = {
  Aromantic: '',
  Asexual: '',
  Bisexual: '',
  Gay: '',
  Genderfluid: '',
  Genderqueer: '',
  Intersex: '',
  Lesbian: '',
  Nonbinary: '',
  Pansexual: '',
  Polysexual: '',
  Transgender: '',
};

// ----------------------------------------------------------------------
const playlists = [];
Object.entries(PLAYLIST_DICT).forEach(([playlistName, spotifyUrl]) => {
  playlists.push({
    id: faker.datatype.uuid(),
    cover: `/flags/${playlistName.toLowerCase()}.jpeg`,
    name: playlistName,
    spotifyUrl,
  });
});

export default playlists;