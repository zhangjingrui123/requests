'''
各个接口查询条件及地址
'''

list_roomparams = '''
{
          find_room_type(
            order: "-createdAt"
            skip: 0,
            limit: 10,
            where: {
              and:[
                {
                  flag: "0"
                  hotel_id: 14715551
                  
                  
                }
              ]
            }
          ){
            id
            room_name
            room_area
            room_people_number
            room_floor
            flag
            hotel{
              id
              status
            }
            picture(
              where: {
                picture_type:"room"
              }
            ){
              category
              oss_k
              id
            }
            room_sale_type(
              where: {
                flag:"0"
              }
            ){
              id
              room_sale_name
              room_sale_description
              room_sale_price
              room_sale_amount
              room_sale_status
              room_type{
                id
              }
              flag
            }
            createdAt
            updatedAt
          }
        }
'''
