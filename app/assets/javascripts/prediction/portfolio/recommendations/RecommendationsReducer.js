import { recommendationsConstants } from './RecommendationsConstants';

const recommendations = (state = {}, action) => {

  switch (action.type) {

    case recommendationsConstants.REQUEST:
      return Object.assign({}, state, {
        isFetching: true,
        isFailed: false
      });

    case recommendationsConstants.RECEIVE:
      return Object.assign({}, state, {
        data: action.data,
        isFetching: false,
        isFailed: false
      });

    case recommendationsConstants.FAILURE:
      return Object.assign({}, state, {
        isFailed: true,
        isFetching: false
      });

    default:
      return state
  }
};

export default recommendations;