require 'pg'

conn_wac_db = PG.connect( dbname: 'wac_db' )
conn_wac_local = PG.connect( dbname: 'wac_local' )

users = []
user_fields = ['speaker_image', 'first_name', 'last_name', 'email', 'twitter', 'title', 'organization']

conn_wac_db.exec( "SELECT id FROM wp_posts WHERE post_parent = 0" ) do |result|
  result.each_row do |row|
    conn_wac_db.exec( "SELECT meta_key, meta_value FROM wp_postmeta WHERE post_id=#{row[0]}") do |res|
      user = {}
      res.each do |row|
        user[row['meta_key']] = row['meta_value']
      end
      users << user.select { |k,v| user_fields.include? k }
    end
  end
  users.delete_if { |user| user["email"].nil? }
end

conn_wac_local.prepare('insert_user', 'INSERT INTO "user" (email, password) VALUES ($1, $2) RETURNING id')
conn_wac_local.prepare('insert_profile', 'INSERT INTO profile ("user", "firstName", "lastName", position, organization, twitter, image) VALUES ($1, $2, $3, $4, $5, $6, $7)')

user_count = 0

users.map do |user|
  begin
    user_result = conn_wac_local.exec_prepared('insert_user', [user["email"], ""])
    user_id = user_result[0]['id']

    image_result = conn_wac_db.exec("SELECT post_name FROM wp_posts WHERE id=#{user['speaker_image']}")
    image_name = "#{image_result[0]['post_name']}.jpg"

    conn_wac_local.exec_prepared('insert_profile', [
      user_id,
      user['first_name'],
      user['last_name'],
      user['title'],
      user['organization'],
      user['twitter'],
      image_name
      ])

    user_count += 1
    p "Added user with email #{user['email']}"
  rescue => e
    p "------ Unable to add user with email #{user['email']} -- #{e} ------"
  end

  p "-----------------------------------"
  p "Finished! Added #{user_count} users."
  p "-----------------------------------"
end


